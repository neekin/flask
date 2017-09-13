from config import config
from flask import Flask
import flask_restful
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()
# api = flask_restful.Api()
def create_app(config_name):
    app = Flask(__name__)
    # 绑定 restful资源
    api = flask_restful.Api(app)
    #读取配置文件
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #初始化app
    db.init_app(app)
    login_manager.init_app(app)
    api.init_app(app)
    
    # 附加路由和自定义错误页面
    from app.photos import photos as photos_blueprint
    from app.admin import admin as admin_blueprint
    from app.main import main as main_blueprint
    from app.auth import auth as auth_blueprint

    app.register_blueprint(photos_blueprint,url_prefix='/photos')
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    app.register_blueprint(main_blueprint,url_prefix='/test')
    app.register_blueprint(auth_blueprint,url_prefix='/auth')
    
    from app.HelloWorld.TODO import TodoList,Todo
    api.add_resource(TodoList,'/api/todos')
    api.add_resource(Todo,'/api/todos/<string:todo_id>')

    
    
    return app






# 注册api


# from app.HelloWorld.TODO import TodoList,Todo

# api.add_resource(TodoList,'/api/todos')
# api.add_resource(Todo,'/api/todos/<string:todo_id>')

# #注册蓝图



