from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()  # 实例化登录管理对象


def init_extentions(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    Bootstrap(app)
    # DebugToolbarExtension(app)
    login_manager.init_app(app)  # 初始化应用
    login_manager.login_view = 'auth.login'  # 设置用户登录视图函数
    moment = Moment()
    #  防止csrf注入攻击
    csrf = CSRFProtect()