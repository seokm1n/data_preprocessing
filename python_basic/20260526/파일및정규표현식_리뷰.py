import re

# with open("파일명을 포함한 경로", "접근모드") as fi:
#     fi.read()  # 모든 텍스트 내용을 읽어서 하나의 문자열 객체로 생성
#     fi.readlines()  # 텍스트 파일 각 라인별 내용을 리스트에 항목으로 변환
#     fi.write()  # 텍스트파일에 현재 메모리 내용을 쓰는 함수

# "접근모드" ==> "r", "w", "a", "r+"

# 문자열 객체의 내용을 특정 패턴을 활용해서 찾고(검색), 치환(수정), 분할시키는
# 역할의 문법 ==> 정규표현식
# 패턴 ==> r'[a-z]+' ,

strdata = "AI 프로그래밍 1998 python Preprocessing!!"
print(re.findall(r'[가-힣]+', strdata))  # 한글
print(re.findall(r'[0-9]+', strdata))  # 숫자
print(re.findall(r'[a-zA-Z]+', strdata))  #영어 대소문자
