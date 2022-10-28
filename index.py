from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411017022 吳育樑的的求職相關資訊</h1>"
    homepage += "<a href=/我的個人簡介>我的個人簡介</a><br>"
    homepage += "<a href=/相關相關工作介紹>相關相關工作介紹</a><br>"
    homepage += "<a href=/職涯測驗結果>職涯測驗結果</a><br>"
    homepage += "<a href=/求職自傳履歷>求職自傳履歷</a><br><br>"
    return homepage

@app.route("/me")
def me():
    return render_templates("me.html")

@app.route("/leader")
def leader():
    return render_templates("領頭羊經歷.html")   

@app.route("/work")
def work():
    return render_templates("工作介紹.html")


@app.route("/test")
def test():
    return render_template("職涯結果.html")

@app.route("/job")
def job():
    return render_template("自傳履歷.html")
