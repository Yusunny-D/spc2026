from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 저장소 설정
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    id = request.form.get('username')
    password = request.form.get('password')
    print(f'입력한 ID는 {id}, PW는 {password}')
    return render_template('login.html', name=id)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['photo']
    print(file)
    filename = file.filename # 실습상 사용자가 업로드한 이름을 그대로 쓰지만 실무에서는 overwrite 될 수 있으므로 바꿈!
                             # ex) timestamp, username 등을 덧붙임

    if file and allowed_file(file.filename): # 빈 파일이나 제대로 된 형태의 파일이 안 왔을 때 코드 죽는걸 방지
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return "파일 잘 받음~"
    else:
        return f"지원되지 않는 파일입니다. 파일명: {file.filename}"

if __name__ == '__main__':
    app.run(debug=True)