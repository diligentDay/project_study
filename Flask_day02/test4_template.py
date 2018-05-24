#coding:utf-8
import sys
from flask import Flask, render_template, session, g, flash
reload(sys)
sys.setdefaultencoding("utf-8")
app = Flask(__name__)
app.secret_key = "session"
@app.route('/')
def index():
    my_list = [2,4,3,6,6,]
    my_int =9999 
 
    my_dict_aa = [
            {"name":"laowang","age": 33},
            {"name":"xiaohua","age": 77},
    ]
    temp_dic = {
        "my_list":my_list,
        "my_int":my_int,
        "my_dict_aa":my_dict_aa,
    }
    return render_template("index.html",**temp_dic)
@app.template_filter('db2')
def do_filterdoublesort(ls):
    return ls[::-2]
@app.template_filter('aa')
def do_filterdoublesort(ls):
    ls.reverse()
    return ls
@app.route("/demo5")
def demo5():
    session['name'] = 'xiaohua'
    g.itcast = 'itcast'
    return render_template('index3.html')
@app.route('/demo6')
def demo6():
    flash("哈哈哈")
    return 'success'
    
if __name__ == '__main__':
    app.run(debug=True)

