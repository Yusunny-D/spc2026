from flask import Flask, render_template

from routes.user.user_routes import user_blueprint
from routes.admin_routes import admin_blueprint
from routes.product.product_routes import product_blueprint
from routes.product.product_detail_routes import product_detail_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(admin_blueprint, url_prefix='/admin')
app.register_blueprint(product_blueprint, url_prefix='/product')
app.register_blueprint(product_detail_blueprint, url_prefix='/product_detail')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)