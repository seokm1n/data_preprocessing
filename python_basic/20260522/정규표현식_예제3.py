import re

string_exam = '파이썬, library 활용한 Text Preprocessing'
result = re.findall(r'[a-zA-Z]+',string_exam)

print(result)
