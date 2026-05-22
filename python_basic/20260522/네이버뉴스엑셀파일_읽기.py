import pandas as pd
import re
newsdf = pd.read_excel("navernews.xlsx")
# print(newsdf)
# print(newsdf["뉴스 제목"][0])
for item in newsdf['뉴스 제목']:
    kor_item = re.sub(r'[^ㄱ-힣\s]+','', item)
    print(kor_item)
    print("="*55)