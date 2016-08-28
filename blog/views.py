from blog import app, lm, bcrypt, db
from flask import render_template, redirect, flash, url_for
from .forms import LoginForm, EditForm, PostForm
from .models import User, Post
from flask_login import login_required, login_user, current_user, logout_user
from datetime import datetime
from config import POSTS_PER_PAGE


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    title = "Cherry's Blog"
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.post.data, timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('index'))
    posts = Post.query.paginate(page, POSTS_PER_PAGE, False)
    return render_template('index.html',
                           title=title,
                           form=form,
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
