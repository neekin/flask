from . import main
from flask import render_template,flash,redirect,url_for
from flask_login import current_user
from ..models import User,db,UserLog,Stem
from .forms import StemForm
@main.route("/")
def index():
    form = StemForm()
    stems = Stem.query.order_by(Stem.pub_date.desc()).all()
    print(stems)
    return render_template('/main/index.html',stems=stems,form=form)

@main.route("poststem",methods=['POST'])
def PostStem():
    form = StemForm()
    if form.validate_on_submit():
        print(current_user)
        stem = Stem(user_id=current_user.id,content=form.stem.data)
        db.session.add(stem)
        flash('恭喜你，发布成功！')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form) 