#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
from datetime import datetime

# 현재 디렉토리 기준
base_dir = os.getcwd()

# 오늘 날짜 접두어
today_prefix = datetime.now().strftime("%Y%m%d")
file_to_read = None

# 현재 디렉토리에서 오늘 날짜로 시작하는 엑셀 파일 찾기
for fname in os.listdir(base_dir):
    if fname.startswith(f"토글형식_{today_prefix}") and fname.endswith(".xlsx"):
        file_to_read = os.path.join(base_dir, fname)
        break

# 파일이 없을 경우 종료
if not file_to_read:
    print(f"❌ '{today_prefix}'일자 기준 플레이오토 파일(토글형식)을 현재 폴더에서 찾을 수 없습니다.")
    input("종료하려면 아무 키나 누르세요...")
    sys.exit()

# 파일 읽기 및 변환 진행
playauto_df = pd.read_excel(file_to_read)
print(f"✅ 파일 읽기 완료: {file_to_read}")
print("😎 쭌 파일로 변환 중입니다...")

# 열 순서 재배치 및 컬럼명 변경
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

# 내품수량 계산
df_reordered.loc[:, "내품수량"] = playauto_df["주문수량"] * playauto_df["옵션"]

# 결과 저장
filename = f"쭌_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
save_path = os.path.join(base_dir, filename)
df_reordered.to_excel(save_path, index=False)

print(f"✅ 쭌 파일 저장 완료: {save_path}")


# In[5]:


get_ipython().system('jupyter nbconvert --to script ordering_run.ipynb')


# In[ ]:




