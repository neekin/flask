from flask import render_template,redirect,request,url_for,flash,jsonify
from flask_login import login_user,current_user,login_required,logout_user
from .forms import LoginForm,RegistrationForm
from ..models import User
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print('进眼真他了')
        user = User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('用户名或者密码错误！')       
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('你已经退出登录')
    return redirect(url_for('main.index'))    
    
@auth.route('/register',methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,password=form.password.data)
        db.session.add(user)
        flash('恭喜你，注册成功！')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form) 