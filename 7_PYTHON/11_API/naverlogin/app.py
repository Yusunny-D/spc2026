from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv
import os
import requests

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")
callback_uri = os.getenv("NAVER_REDIRECT_URI")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def naver_login():
    auth_url = (
        f"https://nid.naver.com/oauth2.0/authorize?"
        f'response_type=code&client_id={client_id}'
        f'&redirect_uri={callback_uri}&state=HELLO'
    )

    return redirect(auth_url)

@app.route('/api/naver/callback')
def naver_callback():
    code = request.args.get("code")
    state = request.args.get("state")

    # 이 코드를 네이버한테 확인
    token_url = (
        f'https://nid.naver.com/oauth2.0/token?'
        f'grant_type=authorization_code&client_id={client_id}'
        f'&client_secret={client_secret}&code={code}&state=HELLO'
        )

    token_res = requests.get(token_url).json()
    access_token = token_res.get('access_token')
    print(access_token)

    return "인증은 일단 성공, 당신이 누군진 몰라도 네이버 다녀온건 확인했음"

if __name__=='__main__':
    app.run(debug=True)