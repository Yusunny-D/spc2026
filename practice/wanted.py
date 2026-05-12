from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://www.wanted.co.kr/wdlist')
    
    jobs = page.locator('li.Card_Card__aaatv')
    # print(jobs.count())

    links = []
    
    for i in range(jobs.count()):
        job = jobs.nth(i)
        code = job.locator('a').get_attribute('href')
        url = f'https://www.wanted.co.kr{code}'

        links.append(url)

    i=1
    for link in links:
        page.goto(link)
        # header = page.locator('header')
        title = page.locator('h1.wds-58fmok').inner_text()
        company = page.locator('a.JobHeader_JobHeader__Tools__Company__Link__NoBQI').inner_text()
        req = ''.join(page.locator('span.wds-1pe0q6z').all_inner_texts())
        cont = page.locator('section.JobContent_descriptionWrapper__RMlfm').inner_text().strip()

        print(f'{i+1}\n회사명: {company}\n공고명: {title}\n조건: {req}\n공고문: {cont}\nurl: https://www.jobkorea.co.kr{url}')
        print('='*90, '\n')

        i+=1