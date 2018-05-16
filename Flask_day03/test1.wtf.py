#coding:utf-8
from flask import Flask, render_template, request
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import EqualTo, DataRequired
app = Flask(__name__)
app.secret_key = 'aaaa'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class RegisterForm(FlaskForm):
    username = StringField('账户', validators=[DataRequired()],render_kw={'placeholder':'请输入账户'})
    password = PasswordField('密码',validators=[DataRequired()],render_kw={'placeholder':'请输入密码'})
    password2 = PasswordField('确认密码',validators=[DataRequired(),EqualTo('password','两次密码不一致')],render_kw={'placeholder':'确认密码'})
    submit = SubmitField('提交')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if not all([username,password,password2]):
            flash('参数不完整')
        elif password != password2:
            flash('两次密码不一致')
        else:
            print username,password,password2
            return 'success'
    return render_template('templ_wtf.html')
@app.route('/form',methods=['GET','POST'])
def form():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print username,password,password2
        return 'success'
    else:
        if request.method == 'POST':
            flash('参数错误')
    return render_template('templ_wtf.html',form=register_form)


if __name__ == '__main__':
    app.run(debug=True)
