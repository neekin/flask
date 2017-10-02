from . import main
from flask import render_template,flash,redirect,url_for,jsonify,request
from flask_login import current_user,login_required
from ..models import User,db,UserLog,Stem,HahaPointLog
from .forms import StemForm
@main.route("/")
def index():
    form = StemForm()
    stems = Stem.query.order_by(Stem.pub_date.desc()).all()
    hpls = HahaPointLog.query.filter_by(user_id=current_user.id)
    return render_template('/main/index.html',stems=stems,hpls=hpls,form=form)

@main.route("poststem",methods=['POST'])
@login_required
def PostStem():
    form = StemForm()
    if form.validate_on_submit():
        stem = Stem(user_id=current_user.id,content=form.stem.data)
        db.session.add(stem)
        flash('恭喜你，发布成功！')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form) 

@main.route("gethahapoint",methods=['POST'])
@login_required
def GetHahaPoint():
    stemid = request.form.get('stemid')
    if HahaPointLog.query.filter_by(fromStem_id=stemid,user_id=current_user.id).first() is None:
        hahaPointlog = HahaPointLog(fromStem_id=stemid,user_id=current_user.id)
        db.session.add(hahaPointlog)
        return '获取到笑点'
    else:
        return '已经获取过了'