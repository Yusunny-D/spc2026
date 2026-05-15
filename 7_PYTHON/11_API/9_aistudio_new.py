import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

res = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='나는 20대 개발자야. 오늘 저녁 메뉴 추천해줘.'
    )

print(res.text)