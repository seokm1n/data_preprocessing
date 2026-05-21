name = "홍길동"
age = 50

print("나의 정보 ==> 이름 : {}, 나이 : {}".format(name, age))
print(f"나의 정보 ==> 이름 : {name}, 나이 : {age}")

strData = """python programming
test python prog
python good
"""
print(strData.capitalize())  # p -> P로 바뀐 새로운 문자열 객체가 생성
print(strData.count("python"))

strData1 = "test python programming"
newString = strData1.replace(" ", ",")
print(newString)
result = newString.split(",")  # 문자열 객체를 특정 문자 기준으로 분할
print(result)  # 결과를 리스트로 반환
print(result[2])
print()

string_exam = "kbs , mbc, jtbc ,sbs "
# noComma = string_exam.replace(" ", "")
# result = noComma.split(",")

listData = []
for item in newString:
    listData.append(item.strip())
print(listData)  # ['kbs', 'mbc', 'jtbc', 'sbs']

listData1 = ['kbs', 'mbc', 'jtbc', 'sbs']
newData = "/".join(listData1)
print(newData)

listData3 = "python#test ai programming,study@good"
# listReplace = listData3.replace("#", "").replace(",", " ")
# result = listReplace.split(" ")
# print(result)

import re  # 정규표현식

result = re.sub(r'[#,@]', ' ', listData3)
print(result)

list_exam = []  # == list()
# print(list_exam, type(list_exam))
# list_exam.append()
# list_exam.extend()
data = {} # == dict()
data2 = () # == tuple()

print(list("abcdef"))