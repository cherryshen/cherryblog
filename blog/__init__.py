from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')

bcrypt = Bcrypt(app)

lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)

mail = Mail(app)

with app.app_context():
    db.metadata.create_all(bind=db.engine)

from blog import views, models

