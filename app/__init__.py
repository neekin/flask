from flask import Flask
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)




# 注册api


from app.HelloWorld.TODO import TodoList,Todo

api.add_resource(TodoList,'/api/todos')
api.add_resource(Todo,'/api/todos/<string:todo_id>')

#注册蓝图

from app.photos import photos as photos_blueprint
from app.admin import admin as admin_blueprint
from app.main import main as main_blueprint

app.register_blueprint(photos_blueprint,url_prefix='/photos')
app.register_blueprint(admin_blueprint, url_prefix="/admin")
app.register_blueprint(main_blueprint,url_prefix='/test')

