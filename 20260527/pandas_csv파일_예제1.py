import numpy as np
import pandas as pd
from prettytable import PrettyTable  # 3.3.0 version 설치


def prinf_df(df):
    table = PrettyTable([''] + list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    print(str(table))
    print()


# prinf_df(df)  # df(데이터프레임) 객체를 테이블 형태로 알아서 예쁘게 출력
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 1000)
passdf = pd.read_csv("서울특별시_지하철 승하차 승객수.csv", encoding="CP949")
prinf_df(passdf)
# passdf.info()

# 호선_명칭 기준 ==> 3호선, 7호선, 9호선, 수인선 만 추출

# print(passdf["호선_명칭"].unique())
# subset1 = passdf.loc[passdf["호선_명칭"]=="3호선",:].copy()
# print(subset1)
# subset2 = passdf.loc[passdf["호선_명칭"]=="9호선",:].copy()
# print(subset2)

# condf = pd.concat([subset1, subset2])  # DataFrame 두개 합치기 ==> concat()
# print(condf)

print(passdf["호선_명칭"].isin(["3호선", "7호선", "9호선", "수인선"]))  # 하나라도 []안에  # 있으면 True, 없으면 False
print("=" * 80)

subset = passdf.loc[passdf["호선_명칭"].isin(["3호선", "7호선", "9호선", "수인선"]), :].copy()  # 여러개 할 때 isin
subset.reset_index(drop=True, inplace=True)
prinf_df(subset)
