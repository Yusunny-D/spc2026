from flask import Flask, send_from_directory, request, jsonify
from database import MyDatabase

app = Flask(__name__)
db = MyDatabase()

# 순서 1.
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/create', methods=['POST'])
def create():
    # DOM의 input.values을 js가 JSON문자열로 만들어서 POST로 /create에 보내줌
    data = request.get_json()
    title = data.get('title')
    message = data.get('message')

    # SQL로 저장
    sql = 'INSERT INTO board (title, message) values (?, ?)'
    db.execute(sql, (title, message))
    db.commit()

    return jsonify({'result': 'success'})

@app.route('/list')
def list():
    sql = 'select * from board'
    result = db.execute_fetch(sql)
    dict_list = [{'id': r['id'], 'title': r['title'], 'message': r['message']} for r in result]
    print(dict_list)
    return jsonify(dict_list)

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()
    id = data.get('id')
    print(id)

    if id:
        id = int(id)
        sql = "DELETE FROM board WHERE id=?"
        db.execute(sql, (id,))
        db.commit()

    return jsonify({'result': 'success'})

@app.route('/modify', methods=['POST'])
def modify():
    data = request.get_json()
    id = data.get('id')
    title = data.get('new_title')
    message = data.get('new_message')
    
    print(id, title, message)

    sql = 'UPDATE board SET title=?, message=? WHERE id=?;'
    db.execute(sql, (title, message, id))
    db.commit()
    
    return jsonify({'result': 'success'})

if __name__=="__main__":
    app.run(debug=True)