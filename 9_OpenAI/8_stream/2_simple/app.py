import json
from openai import OpenAI
from dotenv import load_dotenv
import os

from flask import Flask, send_from_directory, request, Response

load_dotenv()
client = OpenAI(api_key = os.getenv('OPENAI_KEY'))

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/stream', methods=['POST'])
def stream():
    user_message = request.json.get('message', '')

    def generate_respons():
        # 좋은 코드는 try except로 감싸주어야 함
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': '당신은 친절한 AI도우미입니다.'},
                {'role': 'user', 'content': user_message}
            ],
            stream=True
        )

        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield content


    return Response((generate_respons()), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True)