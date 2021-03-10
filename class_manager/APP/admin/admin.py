from flask import current_app, request, jsonify, session
from ..models import *
from flask_login import current_user, login_required
from .. import app, db
from . import admin
import json


# admin后台蓝图模块
# 展示全部用户
@admin.route('/show_users', methods=['POST', 'GET'])
@login_required
def show_users():
    pass
    all_accounts = User.query.all()
    # all_students = Student.query.filter(Student.id.in_([student.account for student in all_accounts
    #                                                     if student.type == 'student'])).all()
    # result = [{'account': student.id, 'name': student.name, 'type': 'student'}
    #           for student in all_students]
    # all_instructors = Instructor.query.filter(Instructor.id.in_([instructor.account for instructor in all_accounts
    #                                                              if instructor.type == 'instructor']))
    # result += [{'account': instructor.id, 'name': instructor.name, 'type': 'instructor'}
    #            for instructor in all_instructors]
    # all_admins = Admin.query.filter(Admin.id.in_([admin.account for admin in all_accounts
    #                                               if admin.type == 'admin']))
    # all_superiors = Superior.query.filter(Superior.id.in_([superior.account for superior in all_accounts
    #                                                        if superior.type == 'superior']))
    # result = result + [{'account': admin.id, 'name': admin.name, 'type': 'admin'}
    #                    for admin in all_admins] + \
    #          [{'account': superior.id, 'name': superior.name, 'type': 'superior'}
    #           for superior in all_superiors]
    # return jsonify(result)


# 重置用户密码
@admin.route('/reset_psw', methods=['POST', 'GET'])
@login_required
def reset_psw():
    pass


# 新建用户
@admin.route('/add_user', methods=['POST', 'GET'])
@login_required
def add_user():
    pass


# 删除用户
@admin.route('/delete_user', methods=['POST', 'GET'])
@login_required
def delete_user():
    pass