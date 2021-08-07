import requests
import time
from bs4 import BeautifulSoup


url = "https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&cnt=1000&SortOrder=1&page="
for i in range(1,20):
# 1. 알라딘 국내도서 페이지 가져오기 
    pageUrl = url + str(i)
    response = requests.get(pageUrl)
    html = response.text

# 2. 저자, 책 이름, 저자 내용, 책 이미지 가져오기
    parsedHtml = BeautifulSoup(html, 'html.parser')
    tableList = parsedHtml.select('#Myform .ss_book_box')

    for book in tableList:
        imgUrl = book.select('table')[0].select('img')[0].get('src')
        title = book.select('.ss_book_list')[0].select('ul .bo3')[0].text

        # 핑크색 글씨가 있을때는 2번째, 없을때는 1번째 li를 가져와야 함
        authorIndex = 1;
        if(book.select('.ss_book_list')[0].select('ul .ss_ht1')):
            authorIndex = 2;
            author = book.select('.ss_book_list')[0].select('ul li')[authorIndex].select('a')[0].text
        else:
            author = book.select('.ss_book_list')[0].select('ul li')[authorIndex].select('a')[0].text
        print(imgUrl)
        print(title)
        print(author)

    print(i, '페이지 크롤링 완료...')
    time.sleep(1)

    #하고 싶은 주석