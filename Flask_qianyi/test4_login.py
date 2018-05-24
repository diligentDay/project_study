#coding:utf-8
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/login',methods=['POST'])
def index():
    username = request.form.get('username')
    password = request.form.get('password')
    if not all([username,password]):
        result = {
            "errcode":-2,
            "errmsg":"params error"
            
        }
        return jsonify(result)
    if username == 'itheima' and password == 'python':
        result = {
            "errcode":-1,
            "errmsg":"wrong username or password"
        }
        return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
