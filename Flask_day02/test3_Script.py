#coding:utf-8
from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def index():
    return '窗前明月广'
if __name__ == '__main__':
    manager.run()
