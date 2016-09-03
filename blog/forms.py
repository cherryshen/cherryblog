from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, validators
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


class ContactForm(Form):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")