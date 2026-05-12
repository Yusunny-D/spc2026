# 1. books.toscrape.com 에 접속해서 페이지를 받아온다
# 2. DOM 을 bs4로 구성한다
# 3. 첫 페이지의 도서명, 평점, 가격을 받아온다
# 4. CSV파일로 저장한다.


import requests
from bs4 import BeautifulSoup
import csv

url = 'https://books.toscrape.com/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

# h3 = soup.find_all('h3')

# titles = []
# for elem in h3:
#     title = elem.find('a')
#     titles.append(title)


# print(titles)

books = soup.find_all('article')
# print(books[0])


title = books[0].find_all('a')[0].find('img').attrs['alt']

rating = books[0].find('p')['class'][1]


price = books[0].find('p', class_="price_color").text


books_list = []

for book in books:
    img = book.find('img')

    book_data = {
    'title': img['alt'],
    'rating': book.find('p')['class'][1],
    'price': book.find('p', class_="price_color").text,
    }
    books_list.append(book_data)

filename = "books_list.csv"

with open(filename, 'w', newline='', encoding='utf-8') as file:
    headers = books_list[0].keys()
    csv_wrirter = csv.DictWriter(file, fieldnames=headers)
    csv_wrirter.writeheader()
    csv_wrirter.writerows(books_list)


# ===============================================================
#                            강사님 답
# ===============================================================


url = 'https://books.toscrape.com/'

resp = requests.get(url)
resp.encoding = 'utf=8' # 인코딩으로 유니코드 글씨로 인식시켜 깨진 글자 제거
soup = BeautifulSoup(resp.text, 'html.parser')

books = soup.find_all("article", class_='product_pod')
# books = soup.select("article.product_pod")

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}



filename = "new_books_list.csv"

with open(filename, 'w', newline='', encoding='utf-8') as file:
    headers = ['제목', '평점', '가격']
    csv_wrirter = csv.DictWriter(file, fieldnames=headers)
    csv_wrirter.writeheader()

    for book in books:
        title = book.h3.a['title']
        rating = book.p['class'][1]
        rating_num = rating_map[rating]
        price = book.select_one(".price_color").text
        price = price.replace('£', '')
        csv_wrirter.writerows({title, rating_num, price})   


