# coding: utf8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from  flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Mig'}
    posts = [ # список выдуманных постов
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        },

        {
            'author': { 'nickname': 'Megust' },
            'body': '111в'
        }


    ]
    return render_template("index.html", title = 'Home', user = user, posts = posts )