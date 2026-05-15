import requests

url = 'https://api.github.com/users/lovehyun/repos'

resp = requests.get(url)
repos = resp.json()

# print(data)

data = []

for repo in repos:
    name = repo['name']
    url = repo['html_url']
    desc = repo['description']
    data.append({
        'name': name,
        'url': url,
        'desc': desc
    })

print(f'리포이름: <30, 리포url: <50, 리포설명: <20')    
for d in data:
    print(f'{d["name"]:<30}, {d["url"]:50}')