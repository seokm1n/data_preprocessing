import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # 차트 시각화 라이브러리(패키지)

import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
	rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
	path = "C:/Windows/Fonts/malgun.ttf"
	font_name = font_manager.FontProperties(fname=path).get_name()
	rc('font',family=font_name)
else:
	print("Unknon system...")

# 사전을 활용해서 DataFrame 객체 생성
dictdata = {"Hong": [90, 80, 70, 60, 55], "Kim": [85, 95, 65, 55, 95], "Park": [88, 93, 75, 72, 45],
            "Lee": [55, 66, 77, 92, 65]}
# 위 사전을 활용해서 DataFrame 객체 생성
scoredf = pd.DataFrame(dictdata, index=["Kor", "Eng", "Math", "Music", "Sci"])
print(scoredf)

# 삭제 문법
# 특정 컬럼 하나 삭제할 때 유용 ==> del 키워드
# del scoredf["Park"]
# print(scoredf)

# 특정 컬럼(행)이나 여러개의 컬럼 삭제 메서드 ==> drop
# default 사본 객체 생성, inplace=True ==> 원본 직접 반영, 리턴값 없음
# print("=" * 80)
# print(scoredf.drop(["Hong", "Park"], axis=1, inplace=True))
# print("=" * 80)
# print(scoredf)

# 영어, 음악 삭제
# print("=" * 80)
# scoredf.drop(["Eng", "Music"], inplace=True)
# print(scoredf)

print("=" * 80)
print(scoredf)
scoredf.index = ["국어","영어","수학","음악","과학"]
print("=" * 80)
print(scoredf)

scoredf.plot.bar()
plt.show()