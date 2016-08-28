from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class EditForm(Form):
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=3000)])


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])