from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(255))
    remark = db.Column(db.String(255))