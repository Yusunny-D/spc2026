from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)
app.json.ensure_ascii = False
# SSR (Server Side Rendering)
# 1. /user 라는 경로를 만들고 URL파라미터를 기반으로 사용자를 조회할수 있게 한다.
#    /user는 모든 사용자 /user/1 홍길동 /user/2 김철수 등
# 2. /product 로 쿼리 파라미터를 기반으로 상품을 조회할수 있다
#    /product는 모든 상품, /product?id=101 로 상품 검색 ?name 으로도 상품 검색

# dict 에 dict 는 인덱싱을 통한 빠른 조회 가능 (굳이 for u in users 이런거 안해도 됨)


users = {
    1: {'id': 1, 'name': '홍길동', 'email': 'hong@example.com'},
    2: {'id': 2, 'name': '김철수', 'email': 'kim@example.com'},
    3: {'id': 3, 'name': '이영희', 'email': 'lee@example.com'},
    4: {'id': 4, 'name': '박민수', 'email': 'park@example.com'},
    5: {'id': 5, 'name': '최지은', 'email': 'choi@example.com'}
}

products = {
    101: {'id': 101, 'name': 'Laptop', 'price': 1000},
    102: {'id': 102, 'name': 'Keyboard', 'price': 50},
    103: {'id': 103, 'name': 'Mouse', 'price': 30},
    104: {'id': 104, 'name': 'Monitor', 'price': 200},
    105: {'id': 105, 'name': 'Headphones', 'price': 80}
}

@app.route('/')
def home():
    return render_template('index.html')


# URL경로 방식
# path parameter
@app.route('/user')
@app.route('/user/<int:id>')
def user(id=None):
    return render_template("user.html", id=id, users=users)


# 쿼리스트링 방식
# query parameter
@app.route('/product')
def product():
    id = request.args.get('id', type=int)
    name = request.args.get('name', type=str)

    found = list(products.values()) # products 안에 딕트가 value 들어가 있으니까 
                                    # values()로 접근하고 list로 만듦
    if id:
        found = [p for p in found if p['id'] == id]
    if name:
        found = [p for p in found if p['name'].lower() == name.lower()]

    return render_template("product.html", results=found)
                    # 파이썬의 results 변수를 템플릿에서도 
                    # results라는 이름으로 사용 가능하게 전달


if __name__ == '__main__':
    app.run(debug=True)