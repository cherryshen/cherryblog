import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'wayne-cheng'

basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cshen:hiro1010@cherryblog.ciaes2shtmhx.us-west-2.rds.amazonaws.com:3306/cherrydb'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#for full text search, Whoosh db
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 25

# pagination
POSTS_PER_PAGE = 5

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'cherryyshen@gmail.com'
MAIL_PASSWORD = 'hiro1010'
