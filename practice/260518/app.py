from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

products = [
    {'id': 1, 'name': '피자', 'price': 3000},
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')


if __name__ == '__main__':
    app.run(debug=True)