from flask import Flask, send_from_directory, request, jsonify
import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_KEY'))

app = Flask(__name__, static_folder='static', static_url_path='')
# 폴터 경로와 그 prefix를 결정(변경) 할 수 있음

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=["POST"])
def chat():
    data = request.get_json()
    chat_message = data.get('chatMessage', "")

    gpt_reply = ask_chatgpt(chat_message)

    return jsonify({'reply': f'{gpt_reply}'})

def ask_chatgpt(chat_message):
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'},
            {'role': 'user', 'content': chat_message}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(debug=True)