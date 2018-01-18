from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/yo-joe')
def yo():
    return 'Whaddup, Joe'

@app.errorhandler(404)
def not_found(error):
    return render_template('missing.html'), 404
