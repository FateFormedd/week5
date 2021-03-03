from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    title = "AJ Book | HOME"
    return render_template('index.html')


@app.route('/book')
def book():
    title = "AJ Book | BOOK"
    return render_template('book.html')

@app.route('/register')
def register():
    title = "AJ Book | REGISTER"
    form = UserInfo()
    if request.method == "POST" and form.validate():
        name = form.name.data
        phone = form.phone.data
        address = form.address.data
    return render_template('register.html')