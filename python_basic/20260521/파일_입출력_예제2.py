# 파일입출력 ==> open(), close()
# open() : 파일 개방 ==> 파일을 파일객체화
# close() : 파일객체 해제

f = open("pythondata.txt", "r")
# strdata = f.read() # 텍스트파일에 작성된 모든 내용을 읽어서 문자열 객체로 생성
# strdata = f.readline()  # 텍스트파일 첫번째 한줄만 읽어서 문자열 객체 생성
strdata =  f.readlines()  # 각 라인의 텍스트를 리스트 항목으로 넣어서 리스트로 반환
print(strdata)
