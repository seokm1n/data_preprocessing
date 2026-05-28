import numpy as np
import pandas as pd
import re

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)
tip_df = pd.read_csv("tips.csv")
print(tip_df)
print("=" * 80)

# tips.csv 파일을 읽어서
# gender 컬럼의 'male'을 0으로 'female'을 1로 일괄 변경

tip_df['gender'] = tip_df['gender'].map({'Male': 0, 'Female': 1})
print(tip_df)
print("=" * 80)

# day 컬럼 데이터 중 몇개의 요일이 있는지 체크
print(tip_df['day'].unique())
print(tip_df['day'].value_counts())
print("=" * 80)

# 요일이 'Sat'와 'Thur'인 항목만 추출 출력
subset = tip_df.loc[tip_df['day'].isin(['Sat', 'Thur']),:].copy()
subset.reset_index(drop=True, inplace=True)
print(subset)
print("=" * 80)

# 요일이 'Sat'와 'Thur'인 테이블 인원수의 평균
print(subset['size'].mean())