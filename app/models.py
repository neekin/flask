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
    nickname = db.Column(db.String(255))
    password_hash = db.Column(db.String(128))
    userlogs = db.relationship('UserLog', backref='user')
    stems = db.relationship('Stem',backref='user')
   
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)    
        
        
    def __repr__(self):
        return "<用户: %r>" % self.username
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class UserLog(db.Model):
    # 会员登陆日志
    __tablename__ = 'userlogs'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)
    def __repr__(self):
        return "<UserLog %r>" % self.id
    



class Stem(db.Model):
    __tablename__ = 'stems'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    content = db.Column(db.Text,nullable=False)
    pub_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    def __repr__(self):
        return "<Conent %r>" % self.id