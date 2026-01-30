from flask_jwt_extended import jwt_required
from app import app, mail, SendMessage
from flask import render_template,json,request
from tabulate import tabulate
from flask_mail import Message


@app.get('/checkout')

def checkout():
    return render_template('checkout.html',active_page="checkout")


@app.post('/place_order')
def place_order():
    form = request.form
    fname = form.get('fName')
    lname = form.get('lName')
    email = form.get('email')
    addr = form.get('addr')
    city = form.get('city')
    cart_str = form.get('cart_item')
    cart = json.loads(cart_str)[0]
    chat_id = '@bakler_team'

    table = tabulate(
        tabular_data=[[fname, lname, email, addr]],
        headers = ['FirstName','LastName', 'Email', 'Address']
    )
    item = table

    html = '--------Invoice---------\n'
    html += f'FirstName: {fname}\n'
    html += f'LastName: {lname}\n'
    html += f'Email: {email}\n'
    html += f'Address: {addr}\n'
    html += f'City: {city}\n'
    html += f'------------------------------------\n'
    html += f'{item}\n'


    res = SendMessage(
        chat_id=chat_id,
        message=html
    )

    # send mail to customer
    msg = Message('Invoice From NhaShopper', recipients=[email])
    msg.body = 'This is all product that you ordered'
    message = render_template('mail/invoice.html')
    msg.html = message
    mail.send(msg)

    return f"{res}"


