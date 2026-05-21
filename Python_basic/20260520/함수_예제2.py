def listsumofdata(list):  # 함수정의 --> 함수명(매개변수)
    sumofdata = 0  # 기능구현 ==> arg 참조하는 리스트 항복의 총합을 계산
    for item in list:
        sumofdata += item
    return sumofdata


total = listsumofdata([60, 77, 88, 33])  # 함수호출(전달인자) --> 함수정의로 점프
print('total : ', total)  # 전달한 리스트의 총합을 출력


def addlistdata(list1, list2):
    resultlist = []
    for idx, item in enumerate(list1):  # enumerate ==> 인덱스, 값 반환
        resultlist.append(item + list2[idx])
    return resultlist


result = addlistdata([5, 6, 7, 8], [2, 3, 4, 5])
print('result : ', result)  # [7,9,11,13]


# CheckAlphaData(): 기능 ==> 앞에 전달된 문자열 중 뒤에 전달된 문자의 개수를 파악해서 반환
def CheckAlphaData(string, char):
    cnt = 0
    for item in string:
        if item == char:
            cnt += 1
    return cnt


cnt = CheckAlphaData("python programming", 'p')  # 함수호출
print('cnt : ', cnt)  # 2
