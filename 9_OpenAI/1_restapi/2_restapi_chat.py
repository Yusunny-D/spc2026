import requests
from dotenv import load_dotenv
import os

load_dotenv()

openai_ai_key = os.getenv("OPENAI_KEY")

def ask_chatbot(user_input):
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
    return(final_res)

# print(ask_chatbot('안녕하세요'))
# print(ask_chatbot('오늘은 2026년 5월 5일 어린이날입니다.'))
# print(ask_chatbot('오늘이 무슨 날인가요?'))

while True:
    user_input = input("\n당신의 질문: ").strip()
    if user_input.lower()in ['quit', 'exit', '종료', '끝']:
        print('대화를 종료 중입니다. 안녕히 가세요')
        break
    else:
        print('대화를 생성 중입니다. 잠시만 기다려 주세요.')
        print('챗봇응답: ', ask_chatbot(user_input))
        print('-'*100)