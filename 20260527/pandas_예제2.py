import numpy as np
import pandas as pd

# 2. 리스트를 활용해서 DataFrame 객체를 생성
mydf = mydf = pd.DataFrame([[60, 70, 80], [90, 50, 85], [66, 77, 88]],
                           columns=["국어", "영어", "수학"], index=['a', 'b', 'c'])
print(mydf)
# 컬럼은 ==> 국어, 영어, 수학
# 행 ==> a, b, c
print("=" * 80)

# 3. 넘파이 배열을 활용한 DataFrame 생성
mydf = pd.DataFrame(np.arange(10, 25).reshape(5, 3),
                    columns=['one', 'two', 'three'])  # , index=['a', 'b', 'c', 'd', 'e'])
print(mydf)
print("=" * 80)
# DataFrame 객체 내용 선택(접근) 문법
# 라벨인덱스로 접근 ==> 라벨 인덱서 ==> loc (label location)
# 수치인덱스로 접근 ==> 수치 인덱서 ==> iloc (integer label location)
print(mydf.iloc[[1, 3], :])  # 1,3행 모든열 출력  # fancy indexing
print(mydf.loc[2, 'two'])  # 명시적 인덱스 2 를 라벨로 인식해서 loc가 가능
# print(mydf.loc['c', 'two'])
print("=" * 80)
print(mydf)

#  새로운 'four'라는 컬럼을 추가
# 데이터는 나중에 추가
mydf['four'] = np.nan  # 엑셀의 빈칸 표현 ==> 결측치(Not a Number)
print(mydf)
# mydf.to_excel('mydata.xlsx', index=False)

print("=" * 80)
# 새로운 행 추가
mydf.loc[5] = np.nan
print(mydf.index)
print(mydf)
