#coding:utf-8
from flask import Flask,make_response
from flask import Flask,request
from flask import Flask,session,redirect, url_for,escape,request
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
'''
@app.route('/',methods=['GET'])
def index():
    return 'Hello World'
'''
@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'
@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username','itcast')
    return resp
@app.route('/request')
def resp_cookie():
    resp = request.cookies.get('username')
    return resp
@app.route('/index1')
def index1():
    session['username'] = 'itcast'
    return redirect(url_for('index'))
@app.route('/')
def index():
    return session.get('username')
if __name__ == '__main__':
    app.run(debug=True)

