# # 함수의 스코핑룰
# # 지역공간 변수 ==> 특정 함수 정의 내부에 선언된(등록) 변수
# # 전역공간 변수 ==> 함수 내부가 아닌 공간에 선언된 변수
# # 내장공간 변수(__name__)
#
# def DisplayData():
#     gdata = 33  # gdata 변수를 지역 공간에 등록하고 33으로 초기화
#     # 함수 내부에서는 항상 지역공간에 등록된 변수를 우선시해서 사용
#     print('gdata : ', gdata)  # 변수 사용
#     # 해당 공간 내부에 등록된 변수를 확인 체크 --> locals()
#     print(locals())
#
#
# gdata = 50  # 전역공간 변수
# DisplayData()  # 함수 호출 --> 정의
# print('gdata : ', gdata)
# print(locals())

def DataControl():
    global gdata  # gdata 변수를 지역공간에 등록하지 않고 전역공간에 등록된 변수를 가져다 사용
    gdata += 50  # 전역공간 등록 변수 사용
    print('gdata : ', gdata)
    print(locals())  # ==> {}

gdata = 30
DataControl()
print('gdata : ', gdata)  #80, 함수의 리턴값을 사용할 수 없는 환경

# 전역공간에 등록된 변수 값을 수정하는 방법
# 1. return을 활용한 방법
# 2. global 키워드를 활용