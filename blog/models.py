from hashlib import md5
from blog import db, app
import sys

#
# enable_search = (sys.version_info >= (3, 0))
# if enable_search:
#     import flask_whooshalchemy as whooshalchemy

if sys.version_info >= (3, 0):
    enable_search = False
else:
    enable_search = True
    import flask_whooshalchemy as whooshalchemy


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), index=True, unique=True)
    password = db.Column(db.String(12))
    authenticated = db.Column(db.Boolean, default=False)
    about_me = db.Column(db.String(3000))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/%s?d=mm&s=%d' % \
               (md5(self.email.encode('utf-8')).hexdigest(), size)


class Post(db.Model):
    __tablename__ = 'post'
    __searchable__ = ['title', 'body']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(3000))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)


if enable_search:
    whooshalchemy.whoosh_index(app, Post)