from flask import Flask, render_template, request, json, jsonify ,abort
from products import products as product_list
from Telagram import SendMessage
from flask_mail import Mail, Message
from tabulate import tabulate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, request, jsonify,render_template
from flask_mail import Message
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, get_jwt
)
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'daisdamxd@gmail.com'
app.config['MAIL_PASSWORD'] = 'lhyn fczp ninv xowd'  # Use App Password from Google
app.config['MAIL_DEFAULT_SENDER'] = 'daisdamxd@gmail.com'

mail = Mail(app)

# --- blocklist for revoked JTIs (in-memory demo) ---
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root@localhost:3306/flaskClothes'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# MySQL
# user = nha
# pass = **Aa12345
# database = flaskclothes




SECRET_KEY = "your-secret-key"  # keep this secret
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

REVOKED_JTIS = set()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_data):
    return jwt_data["jti"] in REVOKED_JTIS


import routes


@app.post("/login")
def login():
    username = request.json.get("username", None)
    new_password = request.json.get("password", None)
    sql_str = text("select * from user where username = :username")
    pre_sql = db.session.execute(sql_str, {"username": username}).fetchone()

    if not pre_sql:
        return jsonify({"msg": "Incorrect username or password"}), 401

    # assert False , pre_sql
    user_id = str(pre_sql[0])
    old_password = pre_sql[3]
    # assert False, check_password_hash(old_password, new_password)
    # assert False , f"{user_id}-{old_password}"

    if check_password_hash(old_password, new_password):
        access_token = create_access_token(identity=user_id)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Incorrect username or password2"}), 401


@app.post("/logout")
@jwt_required()  # revoke current access token
def logout():
    jti = get_jwt()["jti"]
    REVOKED_JTIS.add(jti)
    return jsonify(msg="Access token revoked")


@app.post("/me")
@jwt_required()
def me():
    user = get_jwt_identity()
    return jsonify(user=user)



@app.route('/login')
def auth_page():
    return render_template('login.html')  # Your new form










if __name__ == '__main__':
    app.run()
