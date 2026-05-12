import requests
from bs4 import BeautifulSoup

url = 'https://www.example.com'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

title = soup.find('title')
print(title)

headings = soup.find_all('h1')
print(headings)

divs = soup.find_all('div')
print(divs)

for elem in divs:
    link = elem.a
    if link:
        href = link.get('href')
        print("링크 주소는: ", href)
