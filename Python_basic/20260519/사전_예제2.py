import pandas as pd

scoredict = {"kor": [80, 90, 70], "eng": [77, 88, 99], "math": [55, 66, 77]}
print(scoredict)

mydf = pd.DataFrame(scoredict)
print(mydf)

mydf.to_excel("MyDF.xlsx")  # 엑셀 파일로 저장
