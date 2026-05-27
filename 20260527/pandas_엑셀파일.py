from json.decoder import NaN

import numpy as np
import pandas as pd

popdf = pd.read_excel("population_in_seoul.xls")  # 엑셀파일 읽어서 DataFrame 객체로 생성
# 특정 파일을 읽어서 DataFrame 객체로 생성했을 경우 항상 DataFrame 객체의 정보를 확인 필요 ==> info()
popdf.info()  # NaN 데이터 포함하고 있음
# print(popdf.head())  # 첫행 ~ 5행 선택 추출
# print(popdf.tail())  # 마지막 ~ 위로 5행 선택 추출
# print(popdf.sample(5))  # 랜덤으로 5행 추출
print("=" * 80)
print(popdf)
print("=" * 80)
# 행으로는 '합계'가 있는 행 삭제
# 열로는 '고령자' 컬럼 열 삭제
popdf.drop(0, axis=0, inplace=True)
popdf.drop("고령자", axis=1, inplace=True)
print(popdf)
print("=" * 80)

# NaN이 하나라도 있는 행 삭제
# 결측치 검사
# popdf["남자"].isnull()  # isnull(): 항목이 NaN이면 True, 아니면 False
# 불린 배열을 형성
# print(popdf.loc[popdf["남자"].isnull(), :])
# print(popdf.loc[popdf["여자"].isnull(), :])
for col in popdf.columns:
    print("컬럼 : ", col)
    print(popdf.loc[popdf[col].isnull(), :])
    print("=" * 80)

# 결측치가 있는 행을 찾아서 삭제하는 메서드 ==> dropna()
# how = "any" (행에 하나라도 결측치가 있으면 삭제), = "all" (행에 모든 데이터가 NaN일때 삭제)
popdf.dropna(axis=0, how="any", inplace=True)
print(popdf)
print("=" * 80)

# 결측치 삭제 이후 항상 인덱스 초기화
popdf.reset_index(drop=True, inplace=True)
# drop=False(default) ==> 기존 인덱스 컬럼열로 올리고 인덱스 초기화
# drop=True ==> 컬럼열로 올리지 말고 기존 인덱스 삭제
print(popdf)
