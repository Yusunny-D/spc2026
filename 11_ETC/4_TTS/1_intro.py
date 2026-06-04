#  whisper(속삭임) 말을 기반으로 text로 변환(STT Speech-to-text)

import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

text = "안녕하세요. OpenAI의 음성 생성 예제입니다. 한국말을 얼마나 잘하는지 확인 중입니다."


response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text
)

response.write_to_file('output.mp3')
print("생성완료")