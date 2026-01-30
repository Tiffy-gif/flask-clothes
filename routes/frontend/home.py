from app import app
from flask import render_template
from products import products as product_list



@app.get('/')
def index():
    products = product_list
    # arr = [1, 2]
    # print(arr[3])
    return render_template('index.html', products=products, modules='home')