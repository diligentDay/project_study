#coding:utf-8
from flask import Blueprint
app_cart = Blueprint('cart',__name__,static_folder='static',template_folder='templates')
from views import *
