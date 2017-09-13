from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
   # 会员表设计
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)
    username = db.Column(db.String(255),unique=True)
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)    
        
        
    def __repr__(self):
        return "<用户: %r>" % self.name
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# class UserLog(db.Model):
#     # 会员登陆日志
#     __tablename__ = 'userlog'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 外键定义，指向user表的id字段。在user表中也要进行相应的设置
#     ip = db.Column(db.String(100))
#     addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

#     def __repr__(self):
#         return "<UserLog %r>" % self.id




# # 权限
# class Auth(db.Model):
#     __tablename__ = 'auth'
#     id = db.Column(db.Integer, primary_key=True)  # 编号
#     name = db.Column(db.String(100), unique=True)  # 权限名称
#     url = db.Column(db.String(255), unique=True)  # 地址
#     addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

#     def __repr__(self):
#         return "<Auth %r>" % self.name


# # 角色
# class Role(db.Model):
#     __tablename__ = 'role'
#     id = db.Column(db.Integer, primary_key=True)  # 编号
#     name = db.Column(db.String(100), unique=True)  # 角色名称
#     auths = db.Column(db.String(600))  # 权限列表
#     addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

#     def __repr__(self):
#         return "<Role %r>" % self.name

# # 管理员登陆日志
# class AdminLog(db.Model):
#     __tablename__ = 'adminlog'
#     id = db.Column(db.Integer, primary_key=True)
#     admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 外键定义，指向admin表的id字段。在admin表中也要进行相应的设置
#     ip = db.Column(db.String(100))
#     addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

#     def __repr__(self):
#         return "<AdminLog %r>" % self.id

# # 管理员操作日志
# class OpLog(db.Model):
    # __tablename__ = 'oplog'
    # id = db.Column(db.Integer, primary_key=True)
    # admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 外键定义，指向admin表的id字段。在admin表中也要进行相应的设置
    # ip = db.Column(db.String(100)) # 操作ip
    # reason=db.Column(db.String(600)) # 操作原因
    # addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    # def __repr__(self):
    #     return "<OpLog %r>" % self.id


if __name__ =='__main__': # 直接执行models.py文件来生成数据库表
    db.create_all()    