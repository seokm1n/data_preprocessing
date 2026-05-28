import numpy as np
import pandas as pd
import re

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)
passdf = pd.read_csv("서울특별시_지하철 승하차 승객수.csv", encoding="CP949")
print(passdf)
print("=" * 80)


# 문제)
# ==> 호선_명칭 컬럼 데이터 중 숫자 문자가 있는 호선_명칭 데이터만 추출해서 출력
# subset = passdf.loc[passdf["호선_명칭"].isin([str(item) + '호선' for item in range(1, 100)]), :].copy()
def data_select(arg):
    if len(re.findall(r'[0-9]+', arg)) > 0:
        return True
    else:
        return False


# subset = passdf.loc[passdf["호선_명칭"].apply(data_select), :]
subset = passdf.loc[passdf["호선_명칭"].apply(lambda x: len(re.findall(r'[0-9]+', x)) > 0), :]
subset.reset_index(drop=True, inplace=True)
print(subset)
