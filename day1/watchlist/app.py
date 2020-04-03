import os
import sys

from flask import Flask,render_template,flash,redirect,request,url_for
import click
from flask_sqlalchemy import SQLAlchemy # 导入扩展类

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db') liux或mac系统
# 下面是windows的
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭了对模型修改的监控
app.config['SECRET_KEY'] = 'watchlist_dev'

db = SQLAlchemy(app) # 初始化扩展，传入程序实例app

# models
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


# 模板上下文处理函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(user=user)


# views
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        # 验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash('小伙子，你打错了你不知道么？')
            return redirect(url_for('index'))
        # 保存表单数据
        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash('上传成功！')
        return redirect(url_for('index'))
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

# 修改
@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        
        if not title or not year or len(year)>4 or len(title)>60:
            flash('小伙子！你又写错了！')
            return redirect(url_for('index'))
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('更新成功！')
        return redirect(url_for('index'))
    return render_template('edit.html', movie=movie)

# 删除
@app.route('/movie/del/<int:movie_id>', methods=['GET', 'POST'])
def delt(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        flash('删除成功！')
        return redirect(url_for('index'))
    return render_template('del.html', movie=movie)


# # 动态URL
# @app.route('/index/<name>')
# def home(name):
#     return '<h1>Flask，%s来了！</h1>'% name


# 自定义指令
# 新建data.db的数据库初始化命令
@app.cli.command() # 装饰器，注册命令
@click.option('--drop', is_flag=True,help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库完成')

# 向data.db中写入数据的命令
@app.cli.command()
def forge():
    name = 'Dws'
    movies = [
        {'title':'唐探3','year':'2020'},
        {'title':'囧妈','year':'2020'},
        {'title':'缝纫机乐队','year':'2020'},
        {'title':'我的青春期','year':'2020'},
        {'title':'反转人生','year':'2020'},
        {'title':'大千世界','year':'2020'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'],year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('插入数据成功！')

# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    # 返回模板和状态码
    return render_template('404.html'),404



