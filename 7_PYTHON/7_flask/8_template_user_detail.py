from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': '홍길동', 'age': 25, 'phone': '123-456-789'},
    {'name': '김아무개', 'age': 30, 'phone': '123-555-789'},
    {'name': '고길동', 'age': 26, 'phone': '123-888-789'},
    {'name': '박길동', 'age': 40, 'phone': '123-666-789'},
]

@app.route('/')
def index():
    final_html = render_template('users_detail.html', users=users)
    print(final_html)
    return final_html

if __name__ == '__main__':
    app.run(debug=True)