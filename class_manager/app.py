from flask import Flask, render_template  # 导入render_template模块
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand
from flask_script import Manager
from APP import create_app

app = create_app()
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=1122, debug=True)  # 端口号为1122，设置debug为True使其自动reload
    manager.run()


