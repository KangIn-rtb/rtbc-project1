from flask import Flask, render_template, request, make_response,jsonify

app = Flask(__name__)

@app.get("/")
def hoom():
    return render_template("index.html")

@app.get("/api/friend")
def api_friendFunc():
    name=request.args.get("name","").strip()
    age_str=request.args.get("age","").strip()
    if not name:
        return jsonify({"ok":False,"error":"name is required"}),400
    
    if not age_str.isdigit():
        return jsonify({"ok":False,"error":"age is required"}),400
    
    age = int(age_str)
    age_group = f"{(age // 10) * 10}대"
    
    return jsonify({
        "ok":True,
        "name":name,
        "age":age,
        "age_group":age_group,
        "msg": f"{name}님은 {age}살 {age_group}입니다."
    })

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)