#coding=utf-8
from flask import Flask,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField,SubmitField


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:pythonL@127.0.0.1:3306/book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "aaaa"

#实例化SOLAlchemy对象
db = SQLAlchemy(app)
#定义模型类作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    au_book = db.relationship('Book',backref='author')
    def __repr__(self):
        return 'Author:%s' %self.name
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    def __str__(self):
        return 'Book:%s'%(self.name)


class Append(FlaskForm):
    au_info = StringField(validators=[DataRequired()])
    bk_info = StringField(validators=[DataRequired()])
    submit = SubmitField(u'添加')
@app.route('/',methods=['GET','POST'])
def index():
    append_form= Append()
 
    if request.method == 'POST':
        if append_form.validate_on_submit():
            author_name = append_form.au_info.data
            book_name = append_form.bk_info.data
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                try:
                    author = Author(name=author_name)
                    db.session.add(author)
                    db.session.commit()
                    
                    db.book = Book(name=book_name,author_id=author.id)
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    print e
                    flash('数据库加错误')
            else:
                book_name = [book.name for book in author.books]
                if book_name in book_name:
                    flash('该作者已存在相同的书名')
                else:
                    try:
                        book = Book(name=book_name,author_id=author.id)
                        db.session.add(book)
                        db.session.commit()
                    except Exception as e:
                        db.session.rollback()
                        print e
                        flash('数据添加错误')
        else:
            flash('数据输入有问题')

 
    authors = Author.query.all()
    book = Book.query.all()
    return render_template('index.html',authors=authors,book=book,append_form=append_form)
    
if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    #生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    app.run(debug=True)
