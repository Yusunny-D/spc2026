from flask import Flask, render_template, request, session, redirect, url_for

# Session은 안배울거임 =-> 나중엔 이게 DB에서 대체됨

app = Flask(__name__)
app.secret_key = 'my-random-key'

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': '1234'},
    {'name': 'Charlie', 'id': 'CH', 'pw': 'c123'},
]

@app.route('/dashboard')
def welcome():
    user = session.get('user')
    return render_template('dashboard.html', name=user['name'])

@app.route('/')
def home():
    if session.get('user'):
        return redirect(url_for('welcome'))

    return render_template('index.html')


@app.route('/', methods = ['POST'])
def login():

    id = request.form.get('id') # get으로 가져올 때 html에서 name과 일치해야함
    pw = request.form.get('pw')

    user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)
    

    if user:
        session['user'] = user 
        error = None
        return redirect(url_for('home'))
    
    else:
        error = "Invalid ID or PW"

    return render_template('index.html', error=error)

# 1. 사용자가 비밀번호를 바꾸는 기능을 추가한다
# 1-1. method를 POST로 확장
# 1-2. users 안에서 비번 바꾸기
# 1-3. 성공적으로 변경되면 나의 profile에서 확인한다
# 1-4. '비밀번호 변경'을 눌렀을 때 성공적인 변경 되었음을 알려준다 (사용자 피드백)

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('home'))
    
    if request.method == "POST":
        new_pw = request.form.get('new_pw')
        for u in users:
            if u['id'] == user['id']:
                u['pw'] = new_pw
                session['user'] = u # 세션 정보 갱신! (갱신이 안되면 새로고침을 해도 화면이 안달라짐)
                
                change = '비번 변경 성공!'
                # return render_template('profile.html', user=user, change=change)
                return redirect(url_for('profile'))
                    
    return render_template('profile.html', user=user, change = None)

@app.route('/logout')
def logout():
    session.pop('user', None)

    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)