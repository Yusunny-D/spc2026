import os
from dotenv import load_dotenv
from google import genai
import csv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

videos = []

with open('video_state.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        videos.append({
            'title': row['title'],
            'views': row['view count'],
            'likes': row['like count'],
            'comments': row['comment count']
        })

prompt = f"""
다음 유튜브 영상 데이터를 분석해서:
1. 어떤 영상이 가장 인기가 있는지
2. 인기 있는 이유는 무엇인지
3. 어떤 주제가 반응이 좋은지
4. 내가 유튜브 채널을 운영하려고 하면, 어떤 전략이 좋은지

를 자세히 분석해줘

답변은 html로 포메팅을 해줘.

영상 데이터:
{videos}

"""

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt   
)

print(response.text)