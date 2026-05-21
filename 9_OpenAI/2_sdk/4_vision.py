import openai
from dotenv import load_dotenv
import os
import base64

load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')
client = openai.OpenAI(api_key=openai_api_key)

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as file:
        base64_bytes = base64.b64encode(file.read()).decode('utf-8')
        return f'data:image/jpeg;base64,{base64_bytes}'

def ask_chatbot(image_path, user_input):
    image_base64 = encode_image_to_base64(image_path)
    
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': '당신은 스포츠 전문가이자 국가대표입니다.'},
            {'role': 'user', 'content': [
                {
                    'type': 'text',
                    'text': user_input
                }, 
                {
                    'type': "image_url",
                    'image_url': {
                        'url': image_base64
                    }
                }
            ]},
        ]
    )

    final_res = response.choices[0].message.content
    return final_res

path='good.jpg'
user='이 이미지의 사람을 인식하지 말고 운동자세를 전문가 입장에서 10점 만점에 몇점인지 수치 알 수 있게 점수를 주고, 피드백해줘봐.'

print(ask_chatbot(path, user))
print('-'*100)

path='bad.jpg'
user='이 이미지의 사람을 인식하지 말고 운동자세를 전문가 입장에서 10점 만점에 몇점인지 수치 알 수 있게 점수를 주고, 피드백해줘봐.'

print(ask_chatbot(path, user))

# while True:
#     user_input = input('\n질문: ').strip()
#     chatbot_res = ask_chatbot(user_input)
#     print('챗봇응답: ', chatbot_res)