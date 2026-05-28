import numpy as np
import pandas as pd
import re

# 출력 옵션 제어
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)

youdf = pd.read_excel("youtube_rank_1000.xlsx")  # 엑셀파일 읽어서 DataFrame 객체로 생성
# print(youdf)
# print(youdf.info())
print(youdf.head(10))
print("=" * 80)

# ChannelName 컬럼 데이터를 정리 ==> 첫번째 단어만 출력
# Boram Tube Vlog [보람튜브 브이로그] ==> Boram
# JYP Entertainment ==> JYP

# 함수를 이용해서 ChannelName 컬럼 데이터 일괄 정리
# 일괄정리 ==> 하나의 문자열 항목만(공백을 기준으로 분할시켜서 첫번째 항목만 선택)
print(youdf.columns)  # 컬럼명 여기서 가져와서 쓰기
youdf["ChannelName"] = youdf["ChannelName"].apply(lambda x: x.split(' ')[0])
print(youdf['ChannelName'])

# 정리가 완료 되면 'youtube_data.xlsx' 파일로 저장
youdf.to_excel('youtube_data.xlsx', index=False)