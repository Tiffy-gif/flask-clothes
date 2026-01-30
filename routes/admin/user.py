from app import app,db
from sqlalchemy import text
from flask import render_template, request, Flask
from model.user import *
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required
from werkzeug.utils import secure_filename
@app.get('/user/list')
def user_list():
    return get_user_info(user_id=0)


@app.get('/user/list/<int:user_id>')
def user_list_by_id(user_id):
    return get_user_info(user_id=user_id)


def get_user_info(user_id: int = 0):
    if user_id == 0:
        sql_str = text("select * from user")
        pre_sql = db.session.execute(sql_str ).fetchall()
        if not pre_sql:
            return {'message': 'User table is emply!'}
        return [dict(row._mapping) for row in pre_sql]

    if user_id != 0:
        sql_str = text("select * from user where id = :user_id")
        pre_sql = db.session.execute(sql_str, {"user_id": user_id}).fetchone()
        if not pre_sql:
            return {'message': 'user not found!'}
        return dict(pre_sql._mapping)


@app.post('/user/create')
def user_create():
    form = request.form
    file = request.files.get('image')
    image = None

    if not form:
        return {'message': 'No form was submitted!'}

    if file and file.filename != '':
        file = request.files['image']
        file_name = f"{form.get('username')}_{form.get('email')}_{secure_filename(file.filename)}"
        file.save(f'./static/img/users-img/{file_name}')
        image = file_name

    user= User(
        username = form['username'],
        email = form['email'],
        password = generate_password_hash(form.get('password')),
        image=image
    )
    db.session.add(user)
    db.session.commit()

    return {
        'message': 'User has been created!',
        'user': get_user_info(user.id)
    },200


@app.delete('/user/delete')
def user_delete():
    form = request.get_json()
    if not form:
        return {'message': 'No form was submitted!'},400

    is_exists = get_user_info(form.get('user_id'))
    if is_exists.get('message'):
        return {'message': 'user not found!'},400

    user = User.query.get(form.get('user_id'))
    db.session.delete(user)
    db.session.commit()
    return {
        'message': 'User has been delete!',
    },200



@app.put('/user/update')
def user_update():
    form = request.form
    if not form:
        return {'message': 'No form was submitted!'},400

    is_exists = get_user_info(form.get('user_id'))
    if is_exists.get('message'):
        return {'message': 'user not found!'},400


    user = User.query.get(form.get('user_id'))
    user.username = form['username']
    user.email = form['email']
    user.password = generate_password_hash(form.get('password'))
    db.session.commit()

    return {
        'message': 'user has been Update!',
    },200
