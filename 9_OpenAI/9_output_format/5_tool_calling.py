import os
import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

def get_weather(city):
    weather = {'서울': '맑음, 22도', '부산': '흐림, 25도', 'LA': '맑음, 27도'}
    return weather.get(city, '해당 도시는 없음')

tools = [
    {
        'type': 'fuction',
        'function': {
            'name': 'get_weather',
            'description' : '특정 도시의 현재 날씨를 조회한다.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'city': {'type': 'string', 'discription': '도시 이름'}
                },
                'required': ['city']
            }
        }
    }
]

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role': 'system', 'content': '질문에 대해 JSON으로만 답하시오'},
        {'role': 'user', 'content': '서울의 날씨를 알려주시오.'},
    ],
    tools=tools,
)

message = response.choices[0].message.content
# print(answer)

if message.tool_calls:
    call = message.tool_calls[0]
    print('모델이 호출하려는 함수: ', call.fuction.name)
    print('모델이 호출하려는 인자: ', json.loads(call.fuction.argument))
# else:
prompt += ']n[n]'

prompt = '서울의 날씨를 알려주시오.'

final_reply = client.chat.completions.create(
     messages=[
        {'role': 'system', 'content': '질문에 대해 JSON으로만 답하시오'},
        {'role': 'user', 'content': prompt},
    ],
    tools=tools,
)
print('최종 답변 메세지: ', final_reply.choieces[0].message.content)