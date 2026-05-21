# 코드의 사이즈가 커지고 큰 프로젝트를 수행해야 할 경우
# 기능 단위로 코드를 분할해서 프로젝트를 완성해야 할 경우 필수적으로
# 기능 단위를 함수화 시켜서 사용해야한다.
# 함수 ==> 라이브러리 함수(print, input), 사용자 정의 함수(직접 구현)
# 함수동작 ==> 함수정의, 함수호출
# 함수호출 ---> 함수정의 부분으로 점프해서 함수정의가 동작하고
# 함수정의에 있는 명령이 모두 종료되면 호출로 다시 되돌아옴

# 함수정의 ==> def 키워드 사용
# def 함수명(매개변수):
#     # 해당 함수가 동작하는 명령들의 집합을 구현
#     # ==> 함수의 기능을 서술
#     pass

# 함수의 기능 : 전달인자로 넘겨온 값을 5 더해서 츌력해야하는 기능
def AddDataFunc(arg):
    # print('result : ', arg + 5)
    # 함수의 반환값이 없을 경우 None 객체를 반환
    # return arg + 5

    # arg 매개변수가 참조하고있는 리스트 모든 항목 총합과 평균
    total = 0
    for item in arg:
        total += item
    avg = total / len(arg)
    return total, avg  # return ==> 값의 반환, 함수 종료 두가지 기능


# 여러개 값 tuple pack기능으로 묶어짐
# data = 1, 2, 3
# a, b, c, = (4, 5, 6)

# 함수호출 ==> 함수명(전달인자), 전달인자 ==> 함수정의 부분으로 던져주는 값
# res = AddDataFunc([5, 6, 7, 8, 9])
# print('res : ', res, type(res))

res_total, res_avg = AddDataFunc([5, 6, 7, 8, 9])
print('total : ', res_total, ', avg : ', res_avg)
