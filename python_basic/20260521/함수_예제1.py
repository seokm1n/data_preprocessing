# 0 ~ 특정 정수까지의 총합을 계산하는 함수
# arg=10 ==> 기본값을 갖는 매개변수(파라미터) 설정 (디폴트 파라미터)
def SumOfIntData(data, arg=10):  # 함수 정의
    total = 0
    for x in range(arg):
        total += x

    print('total : ', total)


SumOfIntData(50, 7)  # 함수 호출


# 전달 인자가 여러개일 경우 처리하는 함수
# *arg ==> 여러개의 전달인자를 하나로 묶어서 받음(tuple로 처리), 그 뒤 파라미터 추가 안됨
def SumOfData(argdata, *arg):
    print(arg, type(arg))
    print(argdata)


SumOfData(3, 5, 6, 7, 8, 9)


# dict 형태 처리 함수
# **arg ==> 딕셔너리 형태로 묶음{'a': 100}
def MyDictFunc(**arg):
    print(arg, type(arg))


MyDictFunc(a=100, b=30, c=90)


def MyDataControl(arg):
    total = 0
    # for item in arg:
    #     total += item[1]

    total = arg[0][1] + arg[1][1] + arg[2][1]

    # for a, b in arg:  # tuple unpack 기능 사용
    #     total += b

    return total

datalist = [(3, 4), (5, 6), (7, 5)]
result = MyDataControl(datalist)
print('result : ', result)  # 4+6+5
