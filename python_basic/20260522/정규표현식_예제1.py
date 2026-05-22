import re  # regular expression, 정규표현식

strdata = "TE 파이썬 Ai PYThon3 Programming97 성장 ㅎㅎ 2026A+ B- C+ ALL In ONe !! 빅테크"

# ^ ==> not (반대)
result = re.findall(r'[^a-zA-Z0-9가-힣]+', strdata)
print(result)

# result = re.search(r'[A-Z]+', strdata)
# print(result)

# 문자열 메서드가 아닌 특정 패턴을 활용해서 특정 문자열을 찾고(검색), 분할하고,
# 치환(삭제) 할 수 있는 정규표현식 메서드를 지원

# 검색 ==> findall(패턴, 찾을 문자열) ==> 패턴에 매칭된 모든 내용을 리스트 형태로 반환

# 영문대문자 패턴 ==> A ~ Z ==> 범위를 활용 A-Z
# [] ==> 여러개의 패턴을 하나로 묶어서 표현할 때 사용하는 메타문자
# + ==> + 기호 앞에 있는 패턴이 하나 이상인 문자를 찾아서 반환하는 메타문자
# result = re.findall(r'[A-Z]+', strdata)
# print(result)

# 영문소문자 패턴
# result = re.findall(r'[a-z]+', strdata)
# print(result)

# 영문대소문자로 이루어진 단어 패턴 ==> 영어로 이루어진 단어만 검색
# result = re.findall(r'[A-Za-z]+', strdata)
# print(result)

# 가-힣 : 완성형 범위
# ㄱ-힣 : 조합형 범위

# 한글이 하나이상 모두 찾아서 출력
# result = re.findall(r'[ㄱ-힣]+', strdata)
# print(result)

# 숫자 문자가 한 이상 모두 찾아서 출력
result = re.findall(r'[0-9]+', strdata)
print(result)

if not result:
    print("없어요~")
else:
    print("있어요~")
# [] ==> False (논리)
# 논리 부정(반대) ==> not
# 논리 and ==> and
# 논리 or ==> or

# \w ==> 임의의 문자
# * ==> 메타문자 기준으로 앞의 패턴이 0개 이상을 매칭
strdata = "Ai반 Ai AiAi구축 Ai프로그램 Ai"
result = re.findall(r'A\w*', strdata)
print(result)
