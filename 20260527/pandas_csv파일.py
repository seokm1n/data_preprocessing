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
# print(passdf)
passdf.info()
# prinf_df(passdf.head())
passdf["기준_날짜"] = pd.to_datetime(passdf["기준_날짜"])  # 문자열 항목 --> 시계열 데이터 바꿈
print("=" * 80)
# print(passdf["기준_날짜"])
passdf.info()
prinf_df(passdf.head())
print("=" * 80)
passdf.set_index("기준_날짜", inplace=True)
prinf_df(passdf.head())
print("=" * 80)
prinf_df(passdf.loc['2024/08/21'])
print("=" * 80)

index_data = pd.date_range(start="2025/12/25", periods=30, freq="D")  # 시계열의 범위 데이터를 생성
# print(index_data)
# print("=" * 80)
mydf = pd.DataFrame(np.arange(30,60), columns=['데이터'], index = index_data)
# print(mydf)
# print("=" * 80)
print(mydf.loc['2025'])