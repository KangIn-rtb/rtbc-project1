from flask import Flask,render_template,request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
# 이미지 저장시 오류 방지
import matplotlib.pyplot as plt
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / 'static' / 'images'

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/showdata")
def showdata():
    df = sns.load_dataset("iris")
    print(df.head())
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)