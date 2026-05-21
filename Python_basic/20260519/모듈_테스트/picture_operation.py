def picture_func():  # 함수 정의
    print("사진 동작 완료")

# 함수 정의가 동작하려면 함수 호출 꼭 필요

# 현재 파일이 실행 모듈일 경우 내부 특수 변수 __name__은 __main__을 가짐
# 해당 파일이 import 되는 모듈일 경우 __name__은 모듈명(파일명)을 가짐

if __name__ == "__main__":
    print("__name__ :", __name__)  # 들여쓰기 tab, 반대 shift + tab
    picture_func()  # 함수호출
