from flask import Flask, redirect, render_template, request, session, url_for

# 1. 쇼핑몰 간단히 구현 (꼭 템플릿 엔진 안써도 됨. restapi - flask 해도 무방하고 react - flask 해도 무방함)		
# 	다른거 배운적이 없거나, 또는 개발 시간이나 코드 분량이 가장 적은건 템플릿엔진이 가장 적음	
# 	코드양: React >>> Restapi > 템플릿엔진	
# 1-1. 기본 페이지 및 상품 보기 (미로그인으로도 가능) => 메뉴바는 부트스트랩의 기본 Navbar 그대로..		
# 1-2. 상품을 장바구니에 담으려고 시도하면?? 로그인 안했으면 로그인 유도		
# 1-3. 로그인 후 장바구니에 상품 담고, CRUD 개발 (추가)		
# 1-4. 로그인 후 장바구니에 상품 담고, CRUD 개발 (개별삭제 및 전체 삭제)		
# 1-5. 이쁘게 꾸민것중 "FE<->BE" Flask의 Flash 메시지를 찾아보고 추가 구현		


app = Flask(__name__)
app.secret_key = 'my-random-key'

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': '1234'},
    {'name': 'Charlie', 'id': 'CH', 'pw': 'c123'},
]

products = [
    {'id': '1', 'name': 'apple', 'price': 3000},
    {'id': '2', 'name': 'banana', 'price': 2500},
    {'id': '3', 'name': 'orange', 'price': 4000},
]

@app.route('/')
def home():
    if 'user' not in session:
        user = None
    else:
        user = session['user']
    return render_template('home.html', user=user)

@app.route('/login', methods = ['GET', "POST"])
def login():
    id = request.form.get('id')
    pw = request.form.get('pw')
    user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
    error = None
    
    if request.method == 'POST':
        if user:
            session['user'] = user
            error = error
            return redirect(url_for('home'))
        else:
            error = '아이디 혹은 비번이 잘못되었습니다.'
    
    return render_template('login.html', error=error)

@app.route('/product')
def product():
    if 'user' not in session:
        user = None
    else:
        user = session['user']
    return render_template('product.html', products=products, user=user)

@app.route('/add/<id>')
def add(id):
    # print('함수실행')
    if 'user' not in session:
        return f'<a href="{url_for("login")}">로그인</a> 후 이용해 주세요.'
    
    if 'cart' not in session:
        session['cart'] = {}
    
    if id in session['cart']:
        session['cart'][id] += 1
        session.modified = True
    else:
        session['cart'][id] = 1
        session.modified = True
    
    print(session['cart'])

    return redirect(url_for('product'))

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)