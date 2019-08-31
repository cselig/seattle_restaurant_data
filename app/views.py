from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    errors=[str(e)]
    return render_template('500.html',errors=errors), 500
