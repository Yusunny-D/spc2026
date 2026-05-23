from flask import Flask, send_from_directory, request, session
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')
client = openai.OpenAI(api_key=openai_api_key)

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

system_role = {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'}

def session_database(message):
    chatbot_role = system_role
    if session.get('chat'):
        session['chat'].append(message)
        session.modified = True
    else:
        session['chat'] = [chatbot_role]
        session['chat'].append(message)
        session.modified = True

@app.route('/')
def chatbot():
    return send_from_directory('static', 'index.html')

@app.route('/user_input', methods=['POST'])
def input():
    user_input = request.data.decode('utf-8') # js에서 어떤 데이터 형태로 넘겨주는지 잘 맞춰야함
    user_message = {'role': 'user', 'content': user_input}
    # print(user_input)
    session_database(user_message)

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            system_role,
            user_message
        ]
    )

    final_res = response.choices[0].message.content
    # print(final_res)

    bot_message = {'role': 'assistent', 'content': final_res}
    session_database(bot_message)
    print(session)
    return final_res

if __name__ == '__main__':
    app.run(debug=True)