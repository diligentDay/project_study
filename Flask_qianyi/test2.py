#coding:utf-8
from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = "smtp.126.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "yinqiaoyin@126.com"
app.config['MAIL_PASSWORD'] = "111qqqaaazzz"
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<yinqiaoyin@126.com>'

mail = Mail(app)
@app.route('/')
def index():
    return '<a href="/send_mail">发送邮件</a>'
@app.route('/send_mail')
def send_mail()
    message = Message('我是邮件主题',recipients=['yinqiaoyin@126.com'])
    message.html = '<h1>哈哈啊哈</h1>'
    mail.send(message)
    return '发送中----'

if __name__ == '__main__':
    app.run(debug=True)
