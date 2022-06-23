# web3.py

import urllib.request
from bs4 import BeautifulSoup


# 파일로 저장 
f = open("c:\\work\\webtoon.txt","wt", encoding="utf-8")
    
# 동적으로 주소 생성 
for i in range(1,6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    # 웹페이지의 실행결과를 문자열로 받기 
    data = urllib.request.urlopen(url)
    # 검색할 객체생성 
    soup = BeautifulSoup(data,"html.parser")
    cartoons = soup.find_all("td",class_="title")
    print("개수:{0}".format(len(cartoons)))

    for item in cartoons:
        title = item.find("a").text
        print(title.strip())
        f.write(title.strip() + "\n")

f.close()   
print("웹 크롤링 종료")

# <td class="title">
# <a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>