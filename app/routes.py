from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')
