srcstring = "PYTHON PROGRAMMING"

# result = srcstring.lower()  # 메서드 금지
# 리스트 내포와 조건표현식을 활용해서 구현
# 'A' ==> 65
# 'a' ==> 97
# ord() ==> 문자데이터의 원 수치 데이터를 반환하는 함수
# chr() ==> 원 수치 데이터를 문자데이터로 반환하는 함수

listdata = [chr(ord(s) + 32) if s != " " else s for s in srcstring]
print(listdata)
result = '"' + ''.join(listdata) + '"'
print(result)  # "python programming"

wordlist = ["book", "car", "apple", "python", "ai"]
# wordlist 문자열 항목 중 문자열의 길이가 4 이상인 문자열만 추출
newlist = [word for word in wordlist if len(word) >= 4]  # 필터링(여과기) 구문
print(newlist)

# 동일한 명령을 반복 수행할 경우 사용하는 구문 ==> 반복구문(loop 구문)
# for, while()
for x in [4, 5, 6]:
    print(x)

print("=" * 50)

# 문제1)
# for, range() 활용해서 1~100까지 정수의 합을 계산 출력
total = 0
for x in range(1, 101):
    total += x
print(total)

print("=" * 50)

# 문제2)
# "Python Programming,Ai Agent Programming"이 문자열 중 'g' 문자의
# 개수를 for 반복문 활용해서 계산해서 출력

str1 = "Python Programming,Ai Agent Programming"
# list1 = list(str1)
count = 0;
for x in str1:
    if x == "g":
        count += 1
print(count)

print("=" * 50)

# 문제3)
# 표현할 구구단의 단수를 입력받고 해당 구구단의 내용을 출력 (for 구문 활용)
# 예) 출력할 구구단 단수 입력 : 7
#   7 * 1 = 7
#   ...
dan = int(input("출력할 구구단 단수 입력 : "))
for x in range(1, 10):
    print(dan, "*", x, "=", dan * x)

print("=" * 50)

# 사전 테이터 key, value 교환
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(my_dict)
rev_dict = {}

for key in my_dict:  # for문에 dictionay 사용시 키 값을 사용
    rev_dict[my_dict[key]] = key

print(rev_dict)
