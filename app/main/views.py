from . import main
from flask import render_template,flash,redirect,url_for
from flask_login import current_user,login_required
from ..models import User,db,UserLog,Stem
from .forms import StemForm,GetHahaForm
@main.route("/")
def index():
    form = StemForm()
    hahaForm = GetHahaForm()
    stems = Stem.query.order_by(Stem.pub_date.desc()).all()
    # print(stems)
    return render_template('/main/index.html',stems=stems,form=form,hahaForm=hahaForm)

@main.route("poststem",methods=['POST'])
@login_required
def PostStem():
    form = StemForm()
    if form.validate_on_submit():
        print(current_user)
        stem = Stem(user_id=current_user.id,content=form.stem.data)
        db.session.add(stem)
        flash('恭喜你，发布成功！')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form) 

@main.route("gethahapoint",methods=['POST'])
@login_required
def GetHahaPoint():
    form = GetHahaForm()
    if form.validate_on_submit():
        print(current_user)
        # Stem.query.filter
        # db.session.add(stem)
        flash('获取笑点')
        print('获取笑点')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form) 