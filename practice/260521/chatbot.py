from flask import Flask, send_from_directory, request, session
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')
client = openai.OpenAI(api_key=openai_api_key)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def chatbot():
    return send_from_directory('static', 'index.html')

@app.route('/user_input', methods=['POST'])
def input():
    user_input = request.data.decode('utf-8') # js에서 어떤 데이터 형태로 넘겨주는지 잘 맞춰야함
    print(user_input)
    return '인풋 받음!'

def session_database(user_input, answer):
    chatbot_role = {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'}
    user_message = {'role': 'user', 'content': user_input}
    if session.get('chat'):
        session['chat'].append(user_message)
        session['chat'].append(answer)
    else:
        session['chat'] = [chatbot_role]
        session['chat'].append(user_message)
        session['chat'].append(answer)

def ask_chatbot(user_input):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'},
            {'role': 'user', 'content': user_input}
        ]
    )

    final_res = response.choices[0].message.content
    return final_res

if __name__ == '__main__':
    app.run(debug=True)