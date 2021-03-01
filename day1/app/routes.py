from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
    title = 'AJ Blog | HOME'
    return render_template('index.html', title=title)


@app.route('/top_5')
def top_5():
    title = 'TOP FIVE'
    return render_template('top_5.html', title=title)

