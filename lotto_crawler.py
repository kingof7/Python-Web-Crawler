# requests
# pip install requests
# pip install beautifulsoup4
# beautifulsoup

import requests
from bs4 import BeautifulSoup

for index in range(930,938): #1,2,3,4 회차
    url = f"https://search.daum.net/search?w=tot&DA=LOT&rtmaxcoll=LOT&&q={index}회차%20로또"
    # 위에는 url encoding되서 한글이 깨져보임 -> 임의로 고쳐준것

    req = requests.get(url)

    if req.status_code != requests.codes.ok:
        print("접속 실패")
        continue
    html = BeautifulSoup(req.text, "html.parser") #html에 저장해라

    numbers = html.select("span.ball")

    numbers_list = [number.text for number in numbers]
    print(index)
    print(numbers_list)

'''
for nbr in numbers:
    print(nbr.text)
'''


