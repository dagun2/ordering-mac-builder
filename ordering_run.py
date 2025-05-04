import os
import sys
import pandas as pd
from datetime import datetime

def get_base_dir():
    # 실행파일 또는 스크립트 기준 디렉토리 반환
    if getattr(sys, 'frozen', False):
        return os.path.abspath(os.path.join(os.path.dirname(sys.executable), "../../../"))
    else:
        return os.path.dirname(os.path.abspath(__file__))

# 실행 시작
log = ""
try:
    base_dir = get_base_dir()
    log += f"현재 base_dir: {base_dir}\n"
    today_prefix = datetime.now().strftime("%Y%m%d")

    # 플레이오토 엑셀 찾기
    file_to_read = None
    for fname in os.listdir(base_dir):
        if fname.startswith(f"토글형식_{today_prefix}") and fname.endswith(".xlsx"):
            file_to_read = os.path.join(base_dir, fname)
            break

    if not file_to_read:
        log += f"❌ '{today_prefix}'일자 기준 '플레이오토 파일(토글형식)'을 현재 폴더에서 찾을 수 없습니다.\n"
        raise FileNotFoundError("엑셀 파일 없음")

    log += f"✅ 파일 읽기 완료: {os.path.basename(file_to_read)}\n"
    playauto_df = pd.read_excel(file_to_read)
    log += "😎 쭌 파일로 변환 중입니다...\n"

    # 열 정리
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

    df_reordered["내품수량"] = playauto_df["주문수량"] * playauto_df["옵션"]

    # 저장
    filename = f"쭌_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    save_path = os.path.join(base_dir, filename)
    df_reordered.to_excel(save_path, index=False)
    log += f"✅ 쭌 파일 저장 완료: {filename}\n"

except Exception as e:
    log += f"\n❌ 오류 발생: {str(e)}\n"

# 로그 저장
log_filename = f"쭌_{datetime.now().strftime('%Y%m%d_%H%M%S')}_log.txt"
log_path = os.path.join(get_base_dir(), log_filename)
with open(log_path, "w", encoding="utf-8") as f:
    f.write(log)

# Mac용 자동 로그 파일 열기
# if sys.platform == "darwin":
#     os.system(f"open {log_path}")
