from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/login', methods=['POST'])
def login():
    id = request.form.get('username')
    password = request.form.get('password')
    print(f'입력한 ID는 {id}, PW는 {password}')
    return render_template('login.html', name=id)

if __name__ == '__main__':
    app.run(debug=True)