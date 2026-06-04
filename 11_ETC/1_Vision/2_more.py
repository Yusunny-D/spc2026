# 1. 사진을 직접 올린다 (base64 인코딩)
# 2. 이미지 주소를 주고 읽어가라고 한다.

import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

client = OpenAI()

# image_url='dog.webp'
image_url='juga.jpeg'

def encode_image(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

def ask_about_image(question, b64):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {'type': 'text', "text": question},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}} # 이 줄이 핵심!
            ]
        }
    ]
    )

    return response.choices[0].message.content

# questions = [
#     "이미지에 있는 한글 글자를 다 읽어줘.",
#     "해당 이미지에 사용된 주요 색상을 알려줘.",
#     "이미지의 전체 분위기를 한 문장으로 표현하면?"
# ]
questions = [
    "이 주식 차트를 보고 기술적 분석을 해줘.",
    "이 주식 차트를 보고 매수 또는 매도 시기를 분석해주고 왜 그런지 기술적으로 설명해줘."
]

b64 = encode_image(image_url)
for q in questions:
    print('-'*60)
    print(f'질문: {q}')
    print(f'답변:\n{ask_about_image(q, b64)}')