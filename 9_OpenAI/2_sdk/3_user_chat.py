import openai

from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')
client = openai.OpenAI(api_key=openai_api_key)

def ask_chatbot(user_input):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'},
            {'role': 'user', 'content': user_input},
        ]
    )

    final_res = response.choices[0].message.content
    return final_res

while True:
    user_input = input('\n질문: ').strip()
    chatbot_res = ask_chatbot(user_input)
    print('챗봇응답: ', chatbot_res)