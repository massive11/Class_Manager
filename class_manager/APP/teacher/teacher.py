from flask import current_app, request, jsonify, session
from ..models import *
from flask_login import current_user, login_required
from .. import app, db
from . import teacher
import json


# teacher后台蓝图模块
# 创建课堂
@teacher.route('/create_class', methods=['GET', 'POST'])
@login_required
def create_class():
    pass


# 删除课堂
@teacher.route('/delete_class', methods=['GET', 'POST'])
@login_required
def delete_class():
    pass


# 随机点名
@teacher.route('/choose_stu', methods=['GET', 'POST'])
@login_required
def choose_stu():
    pass

