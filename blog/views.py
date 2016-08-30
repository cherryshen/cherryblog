from blog import app, lm, bcrypt, db
from flask import render_template, redirect, flash, url_for
from .forms import LoginForm, EditForm, PostForm,SearchForm
from .models import User, Post
from flask_login import login_required, login_user, current_user, logout_user
from datetime import datetime
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    title = "Cherry's Blog"
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html',
                           title=title,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user = User.query.first()
    form = LoginForm()
    if form.validate_on_submit():
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect('/index')
    return render_template("login.html",
                           title="Log In",
                           form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    user = current_user
    """Logout the current user."""
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


@lm.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)


@app.route('/about')
def about():
    return render_template('about.html',
                           user=current_user)


@app.route("/edit", methods=['GET','POST'])
@login_required
def edit():
    form = EditForm()
    user = current_user
    if form.validate_on_submit():
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        # flash('Your changes have been saved.')
        return redirect(url_for('edit'))
    return render_template('edit.html', form=form)


@app.route("/post", methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html', form=form)


@app.before_request
def before_request():
    # if current_user.is_authenticated:
        # current_user.last_seen = datetime.utcnow()
    db.session.add(current_user)
    db.session.commit()
    current_user.search_form = SearchForm()


@app.route('/search', methods=['POST'])
def search():
    if not current_user.search_form.validate_on_submit():
        return redirect(url_for('index'))
    return redirect(url_for('search_results', query=current_user.search_form.search.data))


@app.route('/search_results/<query>')
def search_results(query):
    results = Post.query.whoosh_search(query, MAX_SEARCH_RESULTS)
    return render_template('search_results.html',
                           query=query,
                           results=results)
