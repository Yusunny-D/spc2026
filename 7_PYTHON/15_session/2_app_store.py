from flask import Flask, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = "abcd1234" # 이것도 .env에서 다룸
app.config['SESSION_TYPE'] = 'filesystem' # 나의 세션을 파일 / redis / memcahed / mongod 등 다양한 걸 지원
app.config['SESSION_FILE_DIR'] = './.sessions' # 내가 정한 폴더명
app.config['SESSION_PERMANENT'] = False # 브라우저 닫히면 삭제
app.config['SESSION_USE_SIGNER'] = True # 세션 쿠키에 서명 사용



@app.route('/set-session')
def set_session():
    session['username'] = 'spc2026'
    session['fullname'] = '홍길동'
    session['bod'] = '2020/05/05'
    session['hobby'] = '유튜브'

    return "세션 저장 완료"

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f'세션에서 당신의 정보를 찾았습니다. {session['username']}'
    return '세션 정보가 없음'

if __name__ == "__main__":
    app.run(debug=True)