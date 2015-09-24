# coding: utf8
__author__ = 'andrey'
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views