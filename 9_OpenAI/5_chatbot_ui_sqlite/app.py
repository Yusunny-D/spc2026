from flask import Flask, send_from_directory, request, jsonify
import openai
from dotenv import load_dotenv
import os
import sqlite3

conn = sqlite3.connect('chatbot.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

load_dotenv()

client = openai.OpenAI(api_key=os.getenv('OPENAI_KEY'))

app = Flask(__name__, static_folder='static', static_url_path='')

def init_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit

init_db()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=["POST"])
def chat():
    data = request.get_json()
    chat_message = data.get('chatMessage', "")

    cur.execute('INSERT INTO history (role, content) VALUES (?, ?)', ('user', chat_message))
    conn.commit()

    gpt_reply = ask_chatgpt(chat_message)

    cur.execute('INSERT INTO history (role, content) VALUES (?, ?)', ('assistant', gpt_reply))
    conn.commit()

    return jsonify({'reply': f'{gpt_reply}'})

def ask_chatgpt(chat_message):

    cur.execute('SELECT role, content from history ORDER BY id DESC LIMIT 10')
    rows = cur.fetchall()
    rows = rows[::-1]
    
    rows_dict = [{'role': row['role'], 'content': row['content']} for row in rows]
    print('-'* 30)
    print(rows_dict)


    gpt_ask_message = [
        {'role': 'system', 'content': '당신은 나의 질문에 답변을 주는 챗봇입니다.'},
        *rows_dict
    ]

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=gpt_ask_message
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(debug=True)