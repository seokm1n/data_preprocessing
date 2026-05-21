# 문자열 객체 ==> 시퀀스 타입
# 시퀀스 타입 ==> 데이터의 순서가 있는 타입
# 문자열 객체 ==> str()
# 특정 위치를 인덱스로 접근할 수 있음 ==> index는 항상 0부터
from ftplib import print_line

str1 = "python test programming"
print(str1[5])  # [idx] : 인덱싱 문법
print(str1[-1])  # -1 : 마지막 항목의 인덱스

# 슬라이싱 문법
print(str1[7:11])  # [start : stop -1] 까지 잘라냄
print(str1[:6])  # python 만 출력
print(str1[12:])

# 문자열객체에 지원되는 연산 ( +, * )
str2 = "study"
print(str1 + " " + str2)  # 두 문자열을 합쳐줌 (기능추가 오버로딩)

# 문자열 곱셈 연산
print("=" * 50)  # 문자열을 숫자만큼 반복해서 생성
strData = "AI Programming"
for item in strData:
    print(item, end=' ')
print()  # 개행 역할

strData3 = "AI core"  # 문자열 상수 개념
# strData3[0] = 'D';  # 문자열 객체의 항목을 수정할 수 없음 (불변객체)
strData4 = strData3.replace('A', 'D')  # 'A' 문자 'D' 문자로 변경된 새로운 문자열 생성
print(strData3)  # AI core
print(strData4)  # DI core

if 'py' in "python": # "python" 문자열 객체에 "py" 문자열이 있나?
    print("있음")
else :
    print("없음")