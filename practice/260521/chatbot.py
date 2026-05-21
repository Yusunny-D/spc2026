from flask import Flask, send_from_directory, request

app = Flask(__name__)

@app.route('/')
def chatbot():
    return send_from_directory('static', 'index.html')

@app.route('/user_input', methods=['POST'])
def input():
    user_input = request.data.decode('utf-8') # js에서 어떤 데이터타입으로 넘겨주는지 잘 맞춰야함
    print(user_input)
    return '인풋 받음!'

if __name__ == '__main__':
    app.run(debug=True)