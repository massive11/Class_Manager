from exts import db
from flask import session
from flask_login import UserMixin, login_manager


# 账户表
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer(), unique=True, primary_key=True, index=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(16), nullable=False)


# 教师-课堂表
class TeaCourse(db.Model):
    __tablename__ = 'tea_courses'
    course_id = db.Column(db.Integer(), unique=True, primary_key=True, index=True)
    uid = db.Column(db.String(255), nullable=False)
    course_name = db.Column(db.String(255), nullable=False)


# 学生-课堂表
class StuCourse(db.Model):
    __tablename__ = 'stu_courses'
    uid = db.Column(db.Integer(), unique=True, primary_key=True, index=True)
    course_id = db.Column(db.String(255), nullable=False)



