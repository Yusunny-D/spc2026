import requests
from bs4 import BeautifulSoup
import csv


url = 'https://naver.com/'

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

news = soup.select(".")