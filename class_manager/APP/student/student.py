from flask import current_app, request, jsonify, session
from ..models import *
from flask_login import current_user, login_required
from .. import app, db
from . import student
import json


# 加入课堂
@student.route('/add_class', methods=['POST', 'GET'])
@login_required
def add_class():
    pass


# 退出课堂
@student.route('/quit_class', methods=['POST', 'GET'])
@login_required
def quit_class():
    pass