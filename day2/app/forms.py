from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField


class UserInfo(FlaskForm):
    name = StringField('Name')
    phone = StringField('Phone')
    address = TextAreaField('Address')
    submit = SubmitField()