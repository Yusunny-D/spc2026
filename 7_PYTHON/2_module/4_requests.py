import requests

# 외부에 http 요청을 대신 해주는 라이브러리
# resp = requests.get('http://www.example.com/')
# print(resp.text)

resp = requests.get('https://api.github.com')
if resp.status_code == 200:
    print(resp.text)
else:
    print('해당 페이지를 가져오는데 실패했습니다. code: ', resp.status_code)

# current_user_url = resp.text["current_user_url"]
# print(current_user_url)