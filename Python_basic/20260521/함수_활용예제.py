def ReverseData(*arg):
    # global data, value  # 전역공간 등록된 두 변수를 사용
    # data, value = value, data  # temp 쓸 필요 없음

    return arg[1], arg[0]

data = 50
value = 70
print('함수 호출전 : ', data, value)
data, value = ReverseData(data, value)  # 함수 호출
print('함수 호출후 : ', data, value)
