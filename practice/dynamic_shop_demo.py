# 1. 각 페이지마다 상품제목 가격가져오기
# 2. 그 다음에 각 페이지 안의 설명 구매량, 댓글 가져오기
# 3. 로그인후 추가 상품정보 가져오기

# 이후 다음주에는 거기서 LLM 연동해서 가져온 글로 감정분석 등 진행 예정입니다.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://makemyproject.net/shop/')

    # locator로 안 나올 때 몇가지 써볼 방법
    # (CSR, 비동기 렌더링, 동적 렌더링, JS로 DOM 생성, API 기반 렌더링 등)
    # 1. wait_for_selector() -> 해당 selector가 나올 때까지 기다림(안나오면 TimeError)
    # 2. wait_for_load_state('networkidle') -> 네트워크 요청이 거의 끝날 때까지 기다림
    # 3. timeout(n) -> n초 기다림

    # 이 사이트의 경우 비회원인지 회원인지 확인 후 상품 표시
    
    page.wait_for_selector('#products .card') 
    # '#products .card' 이거 있을 때까지 기다려!
    conts = page.locator('#products .card')

    print(conts.count())

# ================================================


# import requests
# from bs4 import BeautifulSoup

# url = 'https://makemyproject.net/shop/'

# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'html.parser')

# # print(soup)

# products = soup.select('#products > div.card')

# print(products)
