import json

from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    ratings = json.load(open('./app/static/data/ratings.json'))
    zip_codes = json.load(open('./app/static/data/zip_codes.geojson'))
    return render_template('home.html', ratings=ratings, zip_codes=zip_codes)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    errors=[str(e)]
    return render_template('500.html',errors=errors), 500
