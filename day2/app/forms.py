from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email


class UserInfo(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone')
    address = TextAreaField('Address')
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField()