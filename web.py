from flask import Flask,Blueprint, request, render_template,jsonify

from orm import db,User
user = Blueprint("user", __name__)
def create_app():
    app = Flask(__name__)
    # 初始化App配置专门针对 SQLAlchemy 进行配置
    # SQLALCHEMY_DATABASE_URI 配置 SQLAlchemy 的链接字符串儿
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@127.0.0.1:3306/homework?charset=utf8'
    # SQLALCHEMY_POOL_SIZE 配置 SQLAlchemy 的连接池大小
    app.config["SQLALCHEMY_POOL_SIZE"] = 5
    # SQLALCHEMY_POOL_TIMEOUT 配置 SQLAlchemy 的连接超时时间
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 15
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # 初始化SQLAlchemy , 本质就是将以上的配置读取出来
    db.init_app(app)
    app.register_blueprint(user)
    return app

@user.route("/")
def index():
    # db.create_all()
    db.session.add(User(name='111')) # 添加
    db.session.commit()
    user_info = User.query(User).filter(User.name == 'name').first() #查询
    print(user_info)
    return jsonify({'user':user_info.name})

if __name__ == '__main__':
    app = create_app()
    app.run(processes=10)
