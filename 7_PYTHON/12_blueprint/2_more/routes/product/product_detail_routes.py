from flask import Blueprint, render_template

product_detail_blueprint = Blueprint('product_detail', __name__)

@product_detail_blueprint.route('/')
def product_detail_page():
    return render_template('product/product_detail.html')