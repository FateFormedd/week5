from app import app
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfo, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required
from werkzeug import check_password_hash


@app.route('/')
@app.route('/index')
def index():
    title = "AJ Book | HOME"
    return render_template('index.html', title=title)


@app.route('/book', methods=['GET', 'POST'])
def book():
    title = "AJ Book | BOOK"
    return render_template('book.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "AJ Book | REGISTER"
    form = UserInfo()
    if request.method == "POST" and form.validate():
        name = form.name.data
        phone = form.phone.data
        address = form.address.data

        new_entry = Book(name, phone, address)
        db.session.add(new_entry)
        db.session.commit()

        new_user = User(name)

    return render_template('register.html', form=form, title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "AJ Book | LOGIN"
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = form.password.data

        user = User.query.filter_by(name=name).first()

        if user is None or not check_password_hash(user.password, password):
            flash("Incorrect email/pass", 'danger')
            return redirect(url_for('login'))

        login_user(user)
        flash("You have logged in")
        return redirect(url_for('index'))
    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have succesfully logged out", 'primary')
    return redirect(url_for('index'))