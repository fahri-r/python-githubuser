from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/search')
def search():
    return render_template('result.html')