# 문제1)
def AlphaFindFunc(msg):
    for i in msg:
        if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
            pass
        else:
            msg = msg.replace(i, '')
    return msg


strdata = "# Ai % 3 pro&*graM"
result = AlphaFindFunc(strdata)
print('result :', result)  # AiprograM ==> 영문 대소문자만 추출 출력
print("=" * 80)


# 문제2)
def WordCountFunc(arg):
    list_dict = {}
    for i in arg:
        if i not in list_dict:
            list_dict[i] = 1
        else:
            list_dict[i] += 1
    return list_dict


listdata = ['python', 'ai', 'study', 'good', 'ai', 'python', 'ai']

result = WordCountFunc(listdata)
print('result : ', result)  # { 'python':2, 'ai':3, 'study':1,'good':1 }
print("=" * 80)


# 문제3)
def InformCombine(key_list, value_list):
    data_dict = {item : value_list[idx] for idx, item in enumerate(key_list)}
    return data_dict

    # data_dict = {}
    # for key, value in zip(key_list, value_list):
    #     if key not in data_dict:
    #         data_dict[key] = value
    # return data_dict


    # for idx, item in enumerate(key_list):
    #     if item not in data_dict:
    #         data_dict[item] = value_list[idx]
    # return data_dict


key_list = ["name", "age", "address"]
value_list = ["Hong", 50, "seoul"]

result = InformCombine(key_list, value_list)
print('result : ', result)  # {'name':"Hong", "age:50, "address":"seoul"}

import os
os.system("pause")
