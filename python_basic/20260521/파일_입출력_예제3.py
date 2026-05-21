# 파일 입출력 ==> with as 구문
with open("pythondata.txt", "r+") as fi:
    str = fi.readlines()  # 전체 문자열 읽기
# with ~ as 구문을 벗어나는 순간 자동 close() --> 메모리 절약
print(str)  # 이미 변수 저장됨
#
strlist = []  # 리스트 내포를 이용해서 \n 없애기
strlist = [item.strip() for item in str]
print(strlist)
