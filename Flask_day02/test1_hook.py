#coding:utf-8
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    print "do something"
    return "index"
    

@app.before_first_request
def before_request():
    print"before_first_request"

@app.before_request
def after_reqiest():
    #response.headers["Content-Type"] = "application/json"
    print"after_request"
    #return response

@app.teardown_request
def teardown_request(e):
    print "teardown_request %s"% e
if __name__ == '__main__':
    app.run(debug=True)
