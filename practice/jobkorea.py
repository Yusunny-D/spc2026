from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1')
    
    jobs = page.locator('tr.devloopArea[data-gno]')
    # print(jobs.count())
        
    for i in range(jobs.count()):
        job = jobs.nth(i)
        company = job.locator('a.normalLog[data-clickctgrcode="B01"]').inner_text()
        # print(company)
        title = job.locator('a.normalLog[data-clickctgrcode="B02"]').inner_text()
        # print(title)
        require = job.locator('p.etc').inner_text()
        # print(require)
        work = job.locator('p.dsc').inner_text()
        # print(work)
        url = job.locator('a.normalLog[data-clickctgrcode="B02"]').get_attribute('href')

        print(f'{i+1}\n회사명: {company}\n공고명: {title}\n조건: {require}\n업무: {work}\nurl: https://www.jobkorea.co.kr{url}')
        print('='*90, '\n')



