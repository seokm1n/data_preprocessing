import re  # regular expression, 정규표현식

strdata = "파이썬,Ai PYThon3#Programming97@성장 빅테크"

# 패턴을 이용해서 특정 문자를 검색 ==> findall()
# 패턴을 이용해서 특정 문자열을 분할 ==> split()
# strdata.split(',') ==> 리스트가 되어버림
# 문자열 메서드로 여러개의 구분자를 활용해 분할하기에는 문제점을 가지고 있음
# 이를 해결하기 위해 패턴을 이용해 문자열을 분할해서 사용


result = re.sub(r'[,\s#@0-9]+', '', strdata)
print(result)

result = re.sub(r'[,\s#@0-9]+', ',', strdata)
print(result)

with open("redata.csv", "w", encoding="UTF-8") as f:
    f.write(strdata)
