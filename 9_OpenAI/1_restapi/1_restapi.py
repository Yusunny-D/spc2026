import requests
from dotenv import load_dotenv
import os

load_dotenv()

openai_ai_key = os.getenv("OPENAI_KEY")
user_input = '강아지 이름 지어줘. 후보 몇 개를 보여줘.'

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    json={
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': '너는 나를 잘 도와주는 경력 20년차 작명가야.'},
            # {'role': 'system', 'content': '너는 나를 잘 도와주는 경력 20년차 실력이 매우 좋은 소프트웨어 개발자야.'},
            # {'role': 'system', 'content': '너는 나를 잘 도와주는 사람이야.'},
            # {'role': 'system', 'content': '너는 나를 잘 도와주는 이탈리안 호텔 쉐프야.'},
            {'role': 'user', 'content': user_input}
            ],
        'temperature': 1.0
    },
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_ai_key}'
    }
)

data = response.json()
final_res = data['choices'][0]['message']['content']
print(final_res)