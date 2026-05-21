# with~as 구문 사용하고 filetest.txt 파일을 읽어서
with open("filetest.txt", "r+") as f:
    str = f.read()
# 마지막 정보 아래와 같이 출력
# ['python', 'test', 'programming', 'study', 'good']
result = [item.strip() for item in str.split(',')]
print(result)


# 문제2)
# R 개수 세기
with open("setup.log", "r+") as fi:
    log_str = fi.read()
log_list = [item for item in log_str]
count = 0
for s in log_list:
    if s == 'R':
        count += 1
print(count)
