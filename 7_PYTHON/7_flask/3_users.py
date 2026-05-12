from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-456-789'},
    {'name': 'Bob', 'age': 30, 'phone': '123-555-789'},
    {'name': 'Charlie', 'age': 27, 'phone': '123-666-789'},
]

# 파이썬의 리스트 form에 딕셔너리로 들어가 있음

@app.route('/')
def main():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    print('사용자 입력값: ', name)
    user = None
    for u in users:
        if u['name'].lower() == name.lower():
            user = u
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': '사용자를 찾지 못했습니다.'})


if __name__ == '__main__':
    app.run(debug=True) 
