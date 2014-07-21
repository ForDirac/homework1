from flask import render_template, Flask, request
from apps import app
import webbrowser

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    get = None
    post = None

    if request.args:
        get = request.args['text_get']
        url1="http://search.naver.com/search.naver?where=nexearch&query=%s&sm=top_hty&fbm=1&ie=utf8"%(get)
        url2="https://www.google.co.kr/webhp?tab=ww&authuser=0&ei=XjrNU4CiOZL68QXB0YK4BQ&ved=0CBQQ1S4#authuser=0&newwindow=1&q=%s"%(get)
        webbrowser.open(url1, 2)
        webbrowser.open(url2, 2)

    return  render_template("index.html", \
        variable_get = get, variable_url1=url1, variable_url2=url2)

