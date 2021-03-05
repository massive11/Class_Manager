from flask import session
from flask_login import UserMixin, login_manager
from class_manager.exts import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash


# 账户表
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    uid = db.Column(db.String(13), unique=True, primary_key=True, index=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    type = db.Column(db.Integer, nullable=False)  # 用户属性： 0.管理员 1.学生 2.教师


# 教师-课堂表
class TeaCourse(db.Model):
    __tablename__ = 'tea_courses'
    # 教师id和课程id共同作为主键
    course_id = db.Column(db.String(6), primary_key=True)
    uid = db.Column(db.String(13), primary_key=True, nullable=False)
    course_name = db.Column(db.String(32), nullable=False)


# 学生-课堂表
class StuCourse(db.Model):
    __tablename__ = 'stu_courses'
    # 学生id和课程id共同作为主键
    uid = db.Column(db.String(13), primary_key=True)
    course_id = db.Column(db.String(6), primary_key=True, nullable=False)



