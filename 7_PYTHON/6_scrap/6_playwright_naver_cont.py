from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://news.naver.com/section/105')
    
    news = page.locator('li._SECTION_HEADLINE')
    # print(news.count())

    links = []
    
    for i in range(news.count()):
        new = news.nth(i)
        # print(new)

        title = new.locator('strong').inner_text()
        urls = new.locator('a.sa_text_title').get_attribute('href')

        # print(f'{i+1}. {title}\n{urls}')

        links.append({
            "title": title,
            'url': urls
        })

        # page.goto(urls)
        # # title = page.locator('h2#title_area').inner_text()
        # print(title)
        # break

    i = 1

    for news in links:
        print(f'{i}. {news['title']}\n{news['urls']}')
        page.goto(news['url'])
        content = page.locator('article#dic_area').inner_text().strip()
        print(content[:100])
        print('본문: ', content)
        i+=1

