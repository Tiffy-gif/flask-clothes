from app import app
from flask import render_template,jsonify ,abort
from products import products as product_list


@app.route('/product/<int:id>')
def detail(id):
    # find the single product with matching id
    product = next((p for p in product_list if p.get("id") == id), None)

    if product:
        # PASS the single product as `product` (not `products`)
        return render_template('detail.html', product=product, modules='detail')
    # fallback if not found
    return render_template('detail.html',product=product,products=product_list,modules='detail')



@app.route('/product/<int:id>')
def product_detail(id):
    product = next((p for p in product_list if p.get("id") == id), None)
    if product:
        # render detail.html and pass variable named "product"
        return render_template('detail.html', product=product)
    # return a 404 if not found
    return render_template('page_error/404.html'), 404


def api_product(id):
    product = next((p for p in product_list if p.get("id") == id), None)
    if product:
        return jsonify(product)
    return abort(404)
