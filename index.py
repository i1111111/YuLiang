from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
 
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411017022 吳育樑的的求職相關資訊</h1>"
    
    homepage += "<a href=/me>我的個人簡介</a><br>"

    homepage += "<a href=/leader>領頭羊經歷</a><br>"
    
    homepage += "<a href=/work>相關工作介紹</a><br>"
    
    homepage += "<a href=/test>職涯測驗結果</a><br>"
    
    homepage += "<a href=/job>求職自傳履歷</a><br><br>"

    homepage += "<a href=/search>選修課程查詢</a><br><br>"

    return homepage

@app.route("/me")
def me():
    return render_template("me.html")

@app.route("/leader")
def leader():
    return render_template("領頭羊經歷.html")   

@app.route("/work")
def work():
    return render_template("工作介紹.html")


@app.route("/test")
def test():
    return render_template("職涯結果.html")

@app.route("/job")
def job():
    return render_template("自傳履歷.html")


@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "POST":
        cond = request.form["keyword"]
        result = "您輸入的課程關鍵字:" + cond
        teacher = request.form["name"]
        result = "您輸入的教師關鍵字:" + teacher

        db = firestore.client()
        collection_ref = db.collection("111")
        docs = collection_ref.get()
        result= ""
        for doc in docs:
            dict = doc.to_dict()
            if cond in dict["Course"] and teacher in dict["Leacture"] :
                result += dict["Leacture"] + "老師開的" + dict["Course"] + "課程,每週"
                result += dict["Time"] + "於" + dict["Room"] + "上課<br>"

        return result
    else:
        result = "抱歉，查無相關條件的選修課程"

if __name__ == "__main__":
    app.run()