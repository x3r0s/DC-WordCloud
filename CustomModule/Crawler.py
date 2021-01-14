import os
import requests
from bs4 import BeautifulSoup as bs4

def Crawl():
    f = open(os.path.join(os.path.dirname(__file__), "../Resource", "data.txt"), mode="w", encoding="utf-8")
    f.write("")
    f.close()
    f = open(os.path.join(os.path.dirname(__file__), "../Resource", "data.txt"), mode="at", encoding="utf-8")

    # User-Agent 설정
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

    for page in range(1, int(input("1~@페이지 : ")) + 1):
        # HTTP GET Request
        response = requests.get("https://gall.dcinside.com/board/lists?id=bike&page={}".format(page), headers=headers)

        # response를 HTML화
        html = response.text
        soup = bs4(html, "html.parser")

        titles = soup.findAll("td", {"class":"gall_tit ub-word"})

        for title in titles:
            # 공지, 설문 게시글 예외처리
            if title.find("em", {"class":"icon_img icon_notice"}) or title.find("em", {"class":"icon_img icon_survey"}):
                pass
            else:
                title = title.find('a').text
                f.write(title + '\n')

if __name__ == "__main__":
    Crawl()