import numpy as np
import pandas as pd
import re
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns  # 시각화 라이브러리(패키지)

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "C:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print("Unknon system...")

# 출력 옵션 제어
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)

youdf = pd.read_excel("youtube_rank_1000.xlsx")  # , index_col=0)  # 엑셀파일 읽어서 DataFrame 객체로 생성
# print(youdf)
# print(youdf.info())
print(youdf.head(10))
print("=" * 80)

youdf["ChannelName"] = youdf["ChannelName"].apply(lambda x: x.split(' ')[0])

# Video 컬럼 데이터 기준 Top 10 항목 추출해서 출력
# 1차 ==> Video 컬럼 데이터를 수치 데이터 모두 반환
youdf['Video'] = youdf['Video'].apply(lambda x: re.sub(r'[,개]', '', x))
print(youdf.head(10))
print("=" * 80)
print(youdf.info())
print("=" * 80)
youdf["Video"] = youdf["Video"].astype("int64")  # 타입 일괄 변환
print(youdf.info())
print("=" * 80)

# 2차 ==> 내림차순 정렬(sort_values)
# ascending=False : 내림차순, =True : 오름차순
youdf.sort_values(by="Video", inplace=True, ascending=False)
# print(youdf.head(30))
# 3차 ==> head(10).copy()
youdf_top10 = youdf.head(10).copy()
print(youdf_top10)
print("=" * 80)

# # ChannelName 컬럼을 인덱스로 설정해주고
# # Video 컬럼만 남게 DataFrame 수정
# youdf_top10 = youdf_top10[['ChannelName','Video']]
# youdf_top10.set_index("ChannelName", inplace=True)
# print(youdf_top10)
# # 수정된 DataFrame 막대차트 시각화
# youdf_top10.plot.bar()
# plt.tight_layout()
# plt.show()
# # plt.savefig("chart1.JPEG")  # 랜더링 된 것 파일로 저장

sns.barplot(data=youdf_top10, x="ChannelName", y="Video", hue='ChannelName', legend=False, palette="Set3")
plt.show()
