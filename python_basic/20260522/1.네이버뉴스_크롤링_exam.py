import requests  # 특정 URL에 웹페이지(HTML) 정보를 요청하는 패키지
from bs4 import BeautifulSoup  # 웹페이지 정보를 파이썬 객체화해서 파싱할 수 있게 지원해주는 패키지
# bs4 패키지 안의 BeautifulSoup 클래스만 사용
import re  # 정규표현식

url = ''  # 웹페이지 요청할 URL 정보

#r = requests.get(url, verify=False)  # 웹페이지 요청

# html = r.content  # r.content Or r.text : 웹페이지 형태
#
# soup = BeautifulSoup(html, 'lxml')  # 파서 지정
#
# # 위 방법과 다른 find_all(), find() 메서드 활용
# newtitlesoup = soup.find_all(class_ = 'news_tit')
