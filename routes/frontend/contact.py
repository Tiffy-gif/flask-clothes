from app import app
from flask import render_template
from products import products as product_list



@app.get('/contact')
def contact():
    return render_template('contact.html',modules='contact',active_page="contact")
