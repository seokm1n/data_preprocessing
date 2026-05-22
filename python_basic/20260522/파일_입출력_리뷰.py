# 텍스트 파일 (.txt)은 파일 입출력 코드로 접근하는게 편함
# 파일 개방함수 ==> open(), 접근할 파일의 경로 + 파일명, 접근모드를 설정
# 접근모드 ==> 'r' (읽기), 'w' (쓰기), 'a' (추가), 'r+' (읽기/쓰기 가능모드)
# 파일 해제함수 ==> close()
# with ~ as 구문을 활용 / with ~ as 구문 블럭을 벗어나면 자동 close됨

with open(mode='r', file="C:/Users/15/python_project/Python_basic/20260521/pythondata.txt") as fi:  # 위치
    # str = fi.read()  # 전체 문자열
    # str = fi.readline()
    str = fi.readlines()
print(str)
listdata = [x.strip() for x in str]
print(listdata)

import pandas as pd
mydf = pd.DataFrame(listdata)
print(mydf)
mydf.to_excel("pythondata.xlsx", index=False)

# import os
# print(os.getcwd())  # 현재 경로 표시
# print(os.listdir("C:/Users/15/python_project/Python_basic/20260521"))  # 경로 내 파일명 리스트 출력
