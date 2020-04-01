from flask import Flask
app = Flask(__name__)

@app.route('/')

@app.route('/dws')
def index():
    return "<h1>Flask，Dws来了！</h1>"

# 动态URL
@app.route('/index/<name>')
def home(name):
    return '<h1>Flask，%s来了！</h1>'% name

