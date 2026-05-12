from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 크롬 실행
    browser = p.chromium.launch(headless=False)


    page = browser.new_page()

    page.goto('https://www.naver.com/')

    print(page.title())

    page.screenshot(path='naver.png')

    input('엔터를 누르면 종료됩니다.')