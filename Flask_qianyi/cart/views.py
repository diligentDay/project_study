from . import app_cart
from flask import render_template

@app_cart.route('/cart_list')
def cart_list():
    return 'cart list'
@app_cart.route('/cart_index')
def cart_index():
    return render_template('cart_index.html')
