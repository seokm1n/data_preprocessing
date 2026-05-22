import requests
from bs4 import BeautifulSoup
import re

# 유튜브 랭킹 페이지
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'

# 헤더 정보
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/136.0.0.0 Safari/537.36'
    )
}

# 웹페이지 요청
r = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(r.text, 'lxml')

# class="subject" 찾기
newtitlesoup = soup.find_all('td', class_='subject')
# print(len(newtitlesoup))
# 제목 정보를 리스트에 취합, 취합하면서 앞뒤 공백 모두 제거 상태로 취합
youtube_title_list = [item.find_all('a')[0].text.strip() for item in newtitlesoup]
print(youtube_title_list)

print("=" * 80)

# 리스트 내포와 정규표현식을 이용해서 위 youtube_title_list 항목을 한줄로 영문 대소문자만 남기도록 수정
result_list = [re.sub(r'[^a-zA-Z\s]+', '', item) for item in youtube_title_list]
print(result_list)

stringdata = '\n'.join(youtube_title_list)

print("=" * 80)

# 정규표현식을 활용해서 전체 문자열 중에 영문 대소문자, 공백만 남기고 삭제
# stringdata_eng = re.findall(r'[\sa-zA-Z]+',stringdata)
# print(''.join(stringdata_eng))

# result = re.sub(r'[^a-zA-Z\s]+','',stringdata)
# print(result)

import pandas as pd

mydf = pd.DataFrame(youtube_title_list, columns=['제목'])
print(mydf)
mydf.to_excel('youtubedata.xlsx', index=False)
# newtitlesoup = soup.find_all('td', class_='subscriber_cnt')  # 구독자수만
