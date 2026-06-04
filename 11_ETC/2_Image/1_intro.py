# 텍스트를 기반으로 이미지르 생성! (GAN)

# 구버전 모델이 dall-e => dall-e => ?
# gpt-image-1.5 또는 gpt-image-2

import base64
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# prompt = """
# 노을 지는 해변, 잔잔한 파도, 인어와 바다의 동물들이 즐겁게 놀고 있는, 
# 특히 행운의 핑크 돌고래가 점프를 하고 있는, 신비로운 분위기, 수채화 스타일
# """
prompt = """
귀여운 손 그림체로 실생활에 쓸 수 있을 법한 코딩에 대한 아이콘팩을 4x4로 16가지 64x64크기로 만들어줘. 
"""

result = client.images.generate(
    model="gpt-image-1.5",
    prompt=prompt,
    size="1024x1024", # 1024x1024, 1024x1536, 1536x1024
    quality='high' # low, medium, high, auto
)

# image-2에서는 4k까지 지원하고(4096). 16:9 비율도 생성함. 지원 언어가 대폭 증가.
        # 단점은 투명배경을 못 만듦... 투명 배경은 1.5의 기능 

b64 = result.data[0].b64_json
with open('output.png', 'wb') as f:
    f.write(base64.b64decode(b64))

print('저장 완료')