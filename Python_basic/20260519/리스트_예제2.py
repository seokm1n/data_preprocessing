listdata1 = [50, 30, 20]
# 시퀀스 객체에 지원하는 연산 ==> +, *, :
listdata2 = [77, 88, 99]

reslist = listdata1 + listdata2
print(reslist)
print(reslist[1:4])

# listtmp = [None] * 10
# print(listtmp)
# listtmp[9] = 40
# print(listtmp)

# listdata3 = [5, 6, 7, 8]
# print(listdata3)

# listdata4 = []
# for item in listdata3:
#     listdata4.append(item + 3)
# print(listdata4)

# import 라이브러리(패키지) 추가하는 문법
# as : 별칭 부여 문법
import numpy as np

arr1 = np.array([99, 22, 33, 55])
print(arr1, type(arr1))
print(arr1 + 3)
import seaborn