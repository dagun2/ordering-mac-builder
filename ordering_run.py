import os
import sys
import pandas as pd
from datetime import datetime
import unicodedata
import traceback

def get_base_dir():
    # .app으로 패키징된 경우
    if getattr(sys, 'frozen', False):
        return os.path.abspath(os.path.join(os.path.dirname(sys.executable), "../../../"))
    else:
        return os.path.dirname(os.path.abspath(__file__))

log = ""
error_log = ""

try:
    base_dir = get_base_dir()
    today_prefix = datetime.now().strftime("%Y%m%d")
    file_to_read = None
    log += f"[경로] base_dir: {base_dir}\n"

    # 파일 탐색 (한글 유니코드 정규화)
    for fname in os.listdir(base_dir):
        normalized_name = unicodedata.normalize("NFC", fname)
        log += f"🔍 검사 중: {normalized_name}\n"
        if normalized_name.startswith(f"토글형식_{today_prefix}") and normalized_name.endswith(".xlsx"):
            file_to_read = os.path.join(base_dir, fname)
            log += "✅ 파일 발견!\n"
            break

    if not file_to_read:
        log += f"❌ '{today_prefix}'일자 기준 토글형식 파일이 없습니다.\n"
        raise FileNotFoundError("엑셀 파일을 찾을 수 없습니다.")

    playauto_df = pd.read_excel(file_to_read)
    log += f"📁 파일 열기 완료: {os.path.basename(file_to_read)}\n"

    df_reordered = playauto_df[[ 
        "주문자명", "수령자명", "수령자휴대폰번호", "수령자전화번호", "주소",
        "배송메세지", "주문수량", "온라인상품명", "쇼핑몰주문번호", "운송장번호",
        "쇼핑몰", "금액", "할인금액", "주문일", "결제완료일"
    ]].copy()

    df_reordered.columns = [
        "구매자성명", "받는사람성명", "받는분전화번호", "기타전화번호", "받는분주소(전체, 분할)",
        "배송메세지1", "내품수량", "품목명", "고객주문번호", "운송장번호",
        "운임구분", "금액", "할인금액", "주문일", "결제완료일"
    ]

    df_reordered["옵션"] = playauto_df["옵션"]

    # 품목 분할 및 수량 분배 처리
    expanded_rows = []

    for _, row in df_reordered.iterrows():
        item_names = [item.strip() for item in str(row["품목명"]).split(",")]

        try:
            order_qty = int(row["내품수량"])
        except:
            order_qty = 1

        try:
            option_val = int(row["옵션"])
        except:
            option_val = 1

        if len(item_names) == 3:
            multipliers = [3, 2, 1]
        elif len(item_names) == 2:
            multipliers = [option_val, 1]
        else:
            row["내품수량"] = option_val * order_qty
            expanded_rows.append(row)
            continue

        for item_name, mul in zip(item_names, multipliers):
            new_row = row.copy()
            new_row["품목명"] = item_name
            new_row["내품수량"] = mul * order_qty
            expanded_rows.append(new_row)

    df_final = pd.DataFrame(expanded_rows)

    # 컬럼 순서 고정
    fixed_columns = [
        "구매자성명", "받는사람성명", "받는분전화번호", "기타전화번호", "받는분주소(전체, 분할)",
        "배송메세지1", "내품수량", "품목명", "고객주문번호", "운송장번호",
        "운임구분", "금액", "할인금액", "주문일", "결제완료일"
    ]
    df_final = df_final[fixed_columns]

    # 저장
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"쭌_{timestamp}.xlsx"
    save_path = os.path.join(base_dir, filename)
    df_final.to_excel(save_path, index=False, sheet_name="이지_업로드", engine="xlsxwriter")
    log += f"✅ 쭌 파일 저장 완료: {filename}\n"

except Exception as e:
    error_log += f"\n❌ 오류 발생: {str(e)}\n"
    error_log += traceback.format_exc()

# 로그 저장 (홈 디렉토리)
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
log_path = os.path.expanduser(f"~/쭌_{timestamp}_log.txt")

with open(log_path, "w", encoding="utf-8") as f:
    f.write(log)

# 에러 로그 저장
if error_log:
    error_log_path = os.path.expanduser("~/ordering_app_error_log.txt")
    with open(error_log_path, 'a', encoding="utf-8") as f:
        f.write(f"\n[{timestamp}] 에러 발생 로그\n")
        f.write(error_log)

# macOS 로그 자동 열기
if sys.platform == "darwin":
    os.system(f"open '{log_path}'")
