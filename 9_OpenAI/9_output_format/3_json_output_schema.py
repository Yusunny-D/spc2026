import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

city_schema = {
    'type': 'object',
    'properies': {
        'name': {'type': 'string'},
        'population': {'type': 'integer'},
        'area_km2': {'type': 'number'},
    },
    'requred': ['name', 'population', 'area_km2'],
    'addtionalProperties': False
}

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': '질문에 대해 JSON으로만 답하시오'},
        {'role': 'user', 'content': '서울의 인구와 면적을 알려주시오.'},
    ],
    response_format={
        'type': 'city_schema',       # 출력 결과가 아래 정의한 나만의 스키마로 주도록 요청
        'json_schema': {
            'name': 'city_info',
            'strict': True,
            'schema': city_schema
        }
        } 
)

answer = response.choices[0].message.content
print(answer)

data = json.load(answer)
print(f"도시의 이름: {data['name']} - 인구: {data['population']:,}명, 면적: {data['area_km2']}km2")