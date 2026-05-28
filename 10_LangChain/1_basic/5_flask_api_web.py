from flask import Flask, request, jsonify, send_from_directory
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

app = Flask(__name__)
llm = ChatOpenAI(model='gpt-4o-mini')

@app.route('/')
def index():
    return send_from_directory("static", "index.html")

@app.route('/api/dinner')
def dinner():
    prompt = [
        SystemMessage(content='당신은 경력 10년차 쉐프입니다.'),
        HumanMessage(content='오늘 저녁 추천해줘.'),
    ]
    result = llm.invoke(prompt)
    # print(result.content)

    return jsonify({'result': 'success', 'chatbot': result.content})

@app.route('/api/name')
def name():
    prompt = [
        SystemMessage(content='You are a creative branding expert.'),
        HumanMessage(content="What's a good company name that makes computer games? Do not give any explanation. Just give me the names."),
    ]
    result = llm.invoke(prompt)
    # print(result.content)

    return jsonify({'result': 'success', 'chatbot': result.content})

@app.route('/api/name', methods=['POST'])
def name2():
    data = request.get_json()
    product = data.get('product')
    user_prompt = f"What's a good company name that makes computer {product}? Do not give any explanation. Just give me the names."


    prompt = [
        SystemMessage(content='You are a creative branding expert.'),
        HumanMessage(content=user_prompt),
    ]
    result = llm.invoke(prompt)
    names = [line.strip() for line in result.content.split('\n')]
    # print(result.content)

    return jsonify({'result': 'success', 'chatbot': names})

if __name__=="__main__":
    app.run(debug=True)




# curl -X POST localhost:5000/api/name -H "Content-Type: application/json" -d '{"product": "sandwich"}'
# curl -X POST localhost:5000/api/name -H "Content-Type: application/json" -d "{\"product\": \"sandwich\"}"
# curl -X POST localhost:5000/api/name -H "Content-Type: application/json" -d "{\"product\": \"beverage\"}"