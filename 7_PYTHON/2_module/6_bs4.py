from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <h1>Title</h1>
    </head>
    <body>
        <p>여기는 첫번째</p>
        <p>여기는 두번째</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

print(soup)

heading = soup.find_all('h1')

print(heading)


