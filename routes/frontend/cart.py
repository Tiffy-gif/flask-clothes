from app import app
from flask import render_template
from products import products as product_list
from flask_jwt_extended import jwt_required

@app.get('/cart')

def cart():
    return render_template('cart.html', modules='cart', active_page="cart")

