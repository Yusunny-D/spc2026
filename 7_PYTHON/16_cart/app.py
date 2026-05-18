from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'hello1234'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

items = [
    {'id': 'item1', 'name': '햄버거', 'price': 5000},
    {'id': 'item2', 'name': '피자', 'price': 8000},
    {'id': 'item3', 'name': '핫도그', 'price': 3000},
]

@app.route('/')
def index():
    return render_template('product.html', items=items)

@app.route('/add_to_cart/<item_id>')
def add_to_cart(item_id):
    print('장바구니에 담을 상품: ', item_id)

    if 'cart' not in session:
        session['cart'] = {}

    if item_id in session['cart']:
        session['cart'][item_id] += 1
    else:
        session['cart'][item_id] = 1

    print(session['cart'])
    session.modified = True

    return redirect(url_for('index'))


@app.route('/cart')
def view_cart():
    cart_items = {}
    total_price = 0
    
    for item_id, quantity in session.get('cart', {}).items():
        item = next((i for i in items if i['id'] == item_id), None)
        cart_items[item_id] = {
            'name': item['name'],
            'quantity': quantity,
            'price': item['price']
        }

        total_price += item['price'] * quantity

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)
    

if __name__ == "__main__":
    app.run(debug=True)