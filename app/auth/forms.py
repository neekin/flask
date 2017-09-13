from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField, SubmitField,DateField,StringField
from wtforms.validators  import DataRequired,Length,Regexp,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    remember_me = BooleanField('保持登录')
    submit = SubmitField('登录')

class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('密　　码', validators=[
        DataRequired(), EqualTo('password2', message='两次密码必须一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经被其他人使用了')