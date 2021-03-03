from app import app
from flask import render_template, request
from app.forms import UserInfo


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
    return render_template('register.html', form=form, title=title)