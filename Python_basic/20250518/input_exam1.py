# # print ==> 문자열 출력
# # input() ==> 키보드로부터 문자열을 입력하는 함수
# # ==> 입력받은 데이터를 문자열 객체 처리
# data1 = int(input("정수 데이터1 입력: ")) # " "문자열을 화면에 출력하고 입력 대기 상태
# data2 = int(input("정수 데이터2 입력: "))
#
# # 문자열 객체 ==> 정수 객체로 변환 : 타입 변환(cast), int()
# print(data1 + data2)

saved_pw = 'python'
count = 1
while True: # 무한 반복 구문
    input_str = input("password 입력(종료:quit) ==> ")
    if input_str == saved_pw:
        print('pw success!!')
        break
    elif input_str == 'quit':
        break # 반복문 탈출
    else:
        print('pw fail!')
        print(f"비밀번호 {count}회 오류")
        count += 1
        if count == 4:
            print("비밀번호 3회 오류로 종료")
            break


