from flask import Flask, render_template, request, make_response,jsonify
import pymysql
app = Flask(__name__)

@app.get("/")
def hoom():
    return render_template("main.html")

@app.get("/legacy")
def legacy():
    pass

@app.get("/async")
def async_f():
    pass

@app.get("/fetch")
def fetch():
    return render_template("show2.html")

@app.get("/axios")
def axios():
    return render_template("show3.html")

@app.get("/api/sangdata")
def sangdata():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="123",
        database="test",
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("select * from sangdata")
    columns = [col[0] for col in cur.description]
    rows = cur.fetchall()
    result = [dict(zip(columns,row)) for row in rows]
    cur.close()
    conn.close()
    return jsonify(result)


if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)