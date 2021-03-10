from flask import Flask, render_template, request, current_app, jsonify, make_response
from flask import Blueprint
from . import main
from ..models import User, TeaCourse, StuCourse
from .. import app, db, login_manager
from flask_login import login_user, logout_user, current_user, login_required


# 首页蓝图模块
# 登录
@main.route('/login', methods=['POST'])
def login():
    data = request.form
    account = data.get('account')
    password = data.get('password')
    remember_me = True
    if account is None or password is None or remember_me is None:
        return jsonify({'message': 'data missing'}), 400
    user = User.query.filter_by(uid=account).first()
    if user is not None:
        if user.password == password:
            login_user(user, remember_me)
            if user.type == 1:
                return jsonify({'type': 'student'})
            if user.type == 2:
                return jsonify({'type': 'teacher'})
            if user.type == 0:
                return jsonify({'type': 'admin'})
            if account in app.config['FLASKY_ADMIN']:
                login_user(user, remember=remember_me)
                return jsonify({'type:root'})
            return jsonify({'message': 'type error'}), 400
        return jsonify({'message': 'password error'}), 403
    return jsonify({'message': 'no account'}), 404


# 登出
@main.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'logout successful'})


# 修改密码
@main.route('/change_passwd', methods=['GET', 'POST'])
@login_required
def change_passwd():
    data = request.form
    u_account = User.query.filter_by(uid=current_user.id).first()
    old_password = u_account.password
    if old_password is None:
        return jsonify({'message': 'no account'}), 404
    if old_password == data.get('old_password'):
        u_account.password = data['new_password']
        db.session.add(u_account)
        db.session.commit()
        return jsonify({'message': 'change successful'})
    else:
        return jsonify({'message': 'password error'}), 403


# 注册
@main.route('/regist')
def regist():
    return render_template('register.html')