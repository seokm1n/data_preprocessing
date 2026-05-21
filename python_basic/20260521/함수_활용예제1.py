def EncryptFunc(msg):
    print(msg)
    for s in msg:
        if s in EncBook:
            msg = msg.replace(s, EncBook[s])
        else:
            s
    return msg


def DecryptFunc(msg):
    # EncBook과 반대된 사전이 필요하다
    DecBook = {}
    for key in EncBook:
        DecBook[EncBook[key]] = key
    # print(DecBook)
    for s in msg:
        if s in DecBook:
            msg = msg.replace(s, DecBook[s])
        else:
            s
    return msg  # 복호화된 문자열


# def DecryptFunc2(msg):
#     for i in msg:
#         if i in EncBook.items()[1]:
#             msg = msg.replace(i, EncBook.items()[0])
#         else:
#             i
#     return msg

stringdata = "I love ai python programming"
EncBook = {'l': '#', 'p': '@', 'o': '7', 'g': '$', 'I': '%', 'a': '8', 't': '*', 'r': '3', 'n': '6'}
encmsg = EncryptFunc(stringdata)  # 전달된 문자열을 암호화 시켜서 반환하는 함수
print(encmsg)  # % #7ve 8i @y*h76 @37$38mmi6$
# 위 암호화된 문자열 다시 복원시키는 함수를 구현
decmsg = DecryptFunc(encmsg)
print(decmsg)
