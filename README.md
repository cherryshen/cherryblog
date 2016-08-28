# cherryblog
This is the contents of config file that I have not added as it contains my secret key. 

import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'make-your-own'

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# pagination
POSTS_PER_PAGE = 5
