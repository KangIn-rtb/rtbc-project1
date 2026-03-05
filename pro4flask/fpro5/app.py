from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def index0():
    return render_template("index.html")

@app.route("/get")
def get():
    return render_template("get.html")

@app.route("/get_result")
def get_result():
    name = request.args.get("username")
    age = request.args.get("age") # 모든 데이터는 문자로 넘어옴
    age = age + "살"
    return render_template("get_result.html",name=name,age=age)

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/post_result", methods=['POST'])
def post_result():
    name = request.form.get("username")
    email = request.form.get("email")
    return render_template("post_result.html",name=name,email=email)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    