from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = 'Dws'
    movies = [
        {'title':'唐探3','year':'2020'},
        {'title':'囧妈','year':'2020'},
        {'title':'缝纫机乐队','year':'2020'},
        {'title':'我的青春期','year':'2020'},
        {'title':'反转人生','year':'2020'},
        {'title':'大千世界','year':'2020'},
    ]
    # return "<h1>Flask，Dws来了！</h1>"
    return render_template('index.html', name=name, movies=movies)

# # 动态URL
# @app.route('/index/<name>')
# def home(name):
#     return '<h1>Flask，%s来了！</h1>'% name

