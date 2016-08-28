from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

bcrypt = Bcrypt(app)

lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)

with app.app_context():
    db.metadata.create_all(bind=db.engine)

from blog import views, models

