import requests
from dotenv import load_dotenv
import os

load_dotenv()

openai_ai_key = os.getenv("OPENAI_KEY")

message = []
message.append({'role': 'system', 'content': '너는 나를 잘 도와주는 사람이야.'},)


def ask_chatbot(user_input):
    global message
    message.append({'role': 'user', 'content': user_input})

    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            json={
                'model': 'gpt-3.5-turbo',
                'messages': message,
                'temperature': 1.0,
            },
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {openai_ai_key}'
            }
        )

        data = response.json()
        final_res = data['choices'][0]['message']['content']
        message.append({'role': 'assistant', 'content': final_res})

        message = [message[0]] + message[-10:]
    except Exception as e:
        print('오류: ', e)
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