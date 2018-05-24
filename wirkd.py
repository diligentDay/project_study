from flask import Flask,json
from flask import redirect
from werkzeug.routing import BaseConverter
class Regex_url(BaseConverter):
    def __init__(self,url_map,*args):
        super(Regex_url,self).__init__(url_map)
        self.regex = args[0]
app = Flask(__name__)
app.url_map.converters['re'] = Regex_url
@app.route('/user/<re("[a-z]{3}"):id>')
def hello_itheima(id):
    return 'hello %s'%id

# @app.route('/')
# def index():
    # return 'hahahaha'
# @app.route('/')
# def hello_2017():
    # return '<h1>hello 2017<h1>'
#@app.route('/user/<int:id>')
#def hello_itheima(id):
    #return 'hello itcast %d' %id

# @app.route('/')
# def hello_itheima():
    # return redirect('http://www.itcast.cn')

# @app.route('/json')
# def do_json():
    # hello={"name":"stranger","say":"hello"}
    # return json.dumps(hello)
# @app.route('/')
# def hello_itheima():
    # return 'hello itcast',666

if __name__ == '__main__':
    app.run()
