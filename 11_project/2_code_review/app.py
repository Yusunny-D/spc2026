from flask import Flask, send_from_directory, jsonify, request
from openai import OpenAI
import os
from dotenv import load_dotenv
import requests

load_dotenv()
app = Flask(__name__, static_folder='public')
my_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=my_key)

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/api/codecheck', methods=['POST'])
def code_check():
    data = request.get_json()
    # print(data)
    # 이걸 넣을건데
    # https://github.com/lovehyun/tutorial-python/blob/main/11.security/1.sqli/app_weak.py
    # 아래처럼 나오게
    # https://raw.githubusercontent.com/lovehyun/tutorial-python/refs/heads/main/11.security/1.sqli/app_weak.py
    # https://raw.githubusercontent.com/lovehyun/tutorial-python/blob/main/11.security/1.sqli/app_weak.py
    
    code_url = data['codeUrl']

    ori_url1 = 'github.com'
    new_url1 = 'raw.githubusercontent.com'

    ori_url2 = 'blob'
    new_url2 = 'refs/heads'


    url = code_url.replace(ori_url1, new_url1).replace(ori_url2, new_url2).strip()
    print(url)

    res = requests.get(url)
    code = res.text


    prompt = (
        "다음 소스코드를 보고 취약점을 분석하시오.\n"
        '각 취약점에 대해 해당 코드의 라인 번호, 코드 스니펫, 취약점 설명과 개선 방안을 간단하게 설명하시오. 코드 내의 주석은 무시해도 됩니다. \n\n'
        '소스코드:\n'
        '-----------\n'
        f'{code}\n'
        '-----------\n'
    )

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '당신은 소스코드 분석 보안 전문가입니다.'},
            {'role': 'user', 'content': prompt}
        ]
    )
    answer = response.choices[0].message.content
    return jsonify({'result': answer})

if __name__ == '__main__':
    app.run(debug=True)