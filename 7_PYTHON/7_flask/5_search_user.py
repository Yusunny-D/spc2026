from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-456-789'},
    {'name': 'Bob', 'age': 30, 'phone': '321-555-789'},
    {'name': 'Charlie', 'age': 25, 'phone': '321-666-789'},
]

@app.route('/search')
def search_user():
    result = users
    # 쿼리 파라미터로 name, age, phone으로 검색하서 결과 반환
    name = request.args.get('name')
    age = request.args.get('age')
    phone = request.args.get('phone')

    if name:
        # if name.lower() == u['name']:
        #     result = u
        #     # return jsonify(result)
        result = [u for u in users if name.lower() == u['name'].lower()] 
    if age:
        result = [u for u in result if int(age) == u['age']] 

            # return jsonify(result)
    if phone:
        result = [u for u in result if u['phone'].startwith(phone)] 

            # return jsonify(result)

    if result:    
        return jsonify(result)
    else:
        return jsonify({'message': 'user not found'})



if __name__ == '__main__':
    app.run(debug=True) 


# http://127.0.0.1:5000/search?q=