from app import app


@app.route('/SendMail')
def send_email():
    return 'Email sent succesfully!'
