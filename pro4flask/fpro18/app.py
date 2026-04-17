from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from db import fetchall_survey,insert_survey
from anal import analysis_func,save_barchart_func
import time

BASE_DIR = Path(__file__).resolve().parent
IMG_PATH = BASE_DIR / 'static' / 'images' / 'vbar.png'
app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")
@app.get("/coffee/survey")
def survey_view():
    return render_template("/coffee/coffee_survey.html")
@app.post("/coffee/surveyprocess")
def surveyprocess():
    gender = (request.form.get("gender") or "").strip()
    age = (request.form.get("age") or "").strip()
    survey = (request.form.get("co_survey") or "").strip()
    if not gender or not survey or not age.isdigit():
        return redirect(url_for("survey_view"))
    age = int(age)
    insert_survey(gender=gender,age=age,co_survey=survey)
    rdata = fetchall_survey()
    crossTab, results, df = analysis_func(rdata)
    if not df.empty:
        save_barchart_func(df, IMG_PATH)
        
    return render_template(
        "coffee/result.html",
        crossTab = crossTab.to_html() if not crossTab.empty else "데이터가 없어요",
        results = results,
        df = df.to_html(index=False) if not df.empty else "",
        chart_path = "images/vbar.png",
        # ts = time.time()
    )

@app.get("/coffee/surveyshow")
def survey_show():
    rdata = fetchall_survey()
    crossTab, results, df = analysis_func(rdata)
    if not df.empty:
        save_barchart_func(df,IMG_PATH)
    return render_template(
        "coffee/result.html",
        crossTab = crossTab.to_html() if not crossTab.empty else "데이터가 없어요",
        results = results,
        df = df.to_html(index=False) if not df.empty else "",
        chart_path = "images/vbar.png",
        # ts = time.time()
    )
    
if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000)
