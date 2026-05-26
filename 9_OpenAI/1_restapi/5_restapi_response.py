import os
import requests
from dotenv import load_dotenv

load_dotenv()

openai_ai_key = os.getenv('OPENAI_KEY')

user_input = '대한민국의 수도는 어디야?'

response = requests.post(
    'https://api.openai.com/v1/responses',
    headers= {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_ai_key}'
    },
    json= {
        'model': 'gpt-4o-mini',
        'input': user_input
    }
)

data = response.json()
print(data)
answer = data['output'][0]['content'][0]['text']
print('-'*60)
print('응답: ', answer)