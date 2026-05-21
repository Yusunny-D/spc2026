from flask import Flask, render_template, redirect, request, session, url_for
from dotenv import load_dotenv
import os
import requests

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")
callback_uri = os.getenv("NAVER_REDIRECT_URI")


naver_token_url = 'https://nid.naver.com/oauth2.0/token'
naver_profile_url = 'https://openapi.naver.com/v1/nid/me'
naver_auth_url = 'https://nid.naver.com/oauth2.0/authorize'

app = Flask(__name__)
app.secret_key = os.getenv("MY_SESSION_KEY")

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/login')
def naver_login():
    auth_url = (
        f"{naver_auth_url}?"
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
        f'{naver_token_url}?'
        f'grant_type=authorization_code&client_id={client_id}'
        f'&client_secret={client_secret}&code={code}&state={state}'
        )

    token_res = requests.get(token_url).json()
    access_token = token_res.get('access_token')
    print(access_token)

    profile_url = (
        f'{naver_profile_url}'
    )

    headers = {'Authorization': f'Bearer {access_token}'}
    profile = requests.get(profile_url, headers=headers).json()
    print('서버측 응답 정보: ', profile)

    session['user'] = profile['response']

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)