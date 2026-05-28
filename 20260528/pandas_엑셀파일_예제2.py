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

# 데이터중에 Category 가 가장 많은 것은?
data = youdf['Category'].value_counts()  # Series

# Series ==> DataFrame 객체로 변환
datadf = pd.DataFrame(data)
print(datadf)
# datadf.index.name = ''
print("=" * 80)
print(datadf)
print("=" * 80)
# count 컬럼명을 카테고리개수 로 수정
datadf.rename(columns={'count': '카테고리개수'}, inplace=True)
print(datadf)
print("=" * 80)
datadf_top5 = datadf.head(5).copy()
print(datadf_top5)

colors = ['#ff9999', '#ffc000', '#8fd9b6', '#d395d0', '#7aa6ff']
wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

plt.pie(x=datadf_top5['카테고리개수'], labels=datadf_top5.index,
        autopct='%.1f%%', startangle=260, counterclock=False,
        colors=colors,
        wedgeprops=wedgeprops, hatch=['**O', 'oO', 'O.O', '.||.', '***'])  # 파이차트 랜더링 함수
plt.show()
