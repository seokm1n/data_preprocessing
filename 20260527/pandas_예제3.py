import numpy as np
import pandas as pd

# 사전을 활용해서 DataFrame 객체 생성
dictdata = {"Hong": [90, 80, 70, 60], "Kim": [85, 95, 65, 55], "Park": [88, 93, 75, 72], "Lee": [55, 66, 77, 92]}
# 위 사전을 활용해서 DataFrame 객체 생성
scoredf = pd.DataFrame(dictdata, index=["Kor", "Eng", "Math", "Music"])
print(scoredf)
# scoredf['subject_total'] = scoredf.loc['Kor'].sum(), scoredf.loc['Eng'].sum(), scoredf.loc['Math'].sum()
# # scoredf['subject_total'] = [int(scoredf.loc[idx].sum())for idx in scoredf.index]
# print(scoredf)
# print(scoredf.columns)
# scoredf.loc['student_mean'] = [scoredf[col].mean() for col in scoredf.columns]
# print(scoredf)

# Kim, Park의 Eng, Math 정보만 출력
# loc 사용, iloc 사용 각각 출력
print("=" * 80)
# scoredf.loc[행인덱스, 열인덱스] ==> 항 위치 데이터만 접근
# scoredf.loc[행슬라이싱, 열슬라이싱] ==> 여러개의 범위 데이터 접근
# label(문자열) 인덱스는 마지막 stop 포함
# 수치(정수) 인덱스는 step-1 까지 포함
# subset = scoredf.loc["Eng":"Math", "Kim":"Park"].copy()
# print(subset)
# # subset DF에서 Park의 Eng 점수 99로 수정
# subset.loc["Eng", "Park"] = 99
# print(subset)
# print(scoredf)

subset = scoredf.iloc[1:3,1:3].copy()
print(subset)
subset.iloc[0,1] = 99
print(subset)
print(scoredf)