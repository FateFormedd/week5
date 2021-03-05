from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfo, LoginForm
from app.models import User, Book
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash


@app.route('/')
@app.route('/index')
def index():
    title = "AJ Book | HOME"
    return render_template('index.html', title=title)


@app.route('/myinfo')
@login_required
def my_info():
    title = "AJ Book | MY INFO"
    return render_template('my_info.html', title=title)


@app.route('/book', methods=['GET'])
def book():
    title = "AJ Book | BOOK"
    book = Book.query.order_by(Book.name.desc()).all()
    return render_template('book.html', title=title)


@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "AJ Book | REGISTER"
    form = UserInfo()
    if request.method == "POST" and form.validate():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        address = form.address.data
        password = form.password.data

        new_entry = Book(name, phone, address)
        db.session.add(new_entry)
        db.session.commit()

        new_user = User(name, email, address, password)
        db.session.add(new_user)
        db.session.commit()

        flash("You have registered", 'success')
        return redirect(url_for('index'))
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
@login_required
def logout():
    logout_user()
    flash("You have succesfully logged out", 'primary')
    return redirect(url_for('index'))


@app.route('/myinfo/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_info(user_id):
    user = User.query.get_or_404(user_id)

    if user.id != current_user.id:
        flash("You cannot delete other people")
        return redirect(url_for('myinfo'))
    db.session.delete(user)
    db.session.commit()
    flash("You have been deleted, have a good day!")
    return redirect(url_for('index'))


@app.route('/myinfo/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_info(user_id):
    user = User.query.get_or_404(user_id)
    update_form = UserInfo()

    if user.id != current_user.id:
            flash("You cant update another users information")
            return redirect(url_for('myinfo'))

    if request.method == 'POST':
        name = update_form.name.data
        email = update_form.email.data
        phone = update_form.phone.data
        address = update_form.address.data

        db.session.commit()
        flash("You have updated your information", 'info')
        return redirect(url_for('index')
    
    return render_template('updateinfo.html', form=update_form)



