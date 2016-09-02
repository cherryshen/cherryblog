from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, HiddenField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class EditForm(Form):
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=3000)])


class PostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    post = TextAreaField('post', validators=[DataRequired()])

class SearchForm(Form):
    search = StringField('search', validators=[DataRequired()])