from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField, SubmitField,DateField,TextField
from wtforms.validators  import DataRequired,Length,Regexp,EqualTo


class StemForm(FlaskForm):
    stem = TextField('梗',validators=[DataRequired()])
    submit = SubmitField('发布')
    
class GetHahaForm(FlaskForm):
    submit = SubmitField('Get')    