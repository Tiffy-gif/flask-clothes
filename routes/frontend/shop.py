from app import app
from flask import render_template
from products import products as product_list
from flask_jwt_extended import jwt_required, get_jwt_identity
@app.get('/shop')
def shop():
    products = product_list
    return render_template('shop.html',products=products, modules='shop',active_page="shop")

