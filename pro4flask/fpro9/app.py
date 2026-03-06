from flask import Flask, render_template, request, make_response, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)

app.secret_key = "abcdef12345"
app.permanent_session_lifetime = timedelta(minutes=5) # 세션 만료 시간 5초 설정 세션 시간이 지나면 자동 로그 아웃

products = [ # json 형식 -> dict 타입
    {"id":1, "name":"노트북","price":3500000},
    {"id":2, "name":"가방","price":73000},
    {"id":3, "name":"RAM","price":430000},
    {"id":4, "name":"키보드","price":55000},
]

@app.route("/")
def product_list():
    return render_template("products.html", products=products)

@app.route("/cart")
def show_cart():
    cart = session.get("cart",{})
    return render_template("cart.html",cart=cart)

@app.route("/add/<int:id>")
def add_cart(id):
    # 세션 cart가 없으면 빈 dict로 생성 
    cart = session.get("cart",{})
    # next(..., None) : 묶음형 자료에서 다음 값 1개를 꺼내는 함수 
    # 주문 상품이 product에 기억됨 
    product = next((p for p in products if p["id"] == id),None)
    
    if product is None: # 없는 상품 id면 이 코드 실행
        return "상품을 찾을 수 없습니다.", 404
    # 상품 있으면 장바구니 추가
    item_name = product["name"]
    if item_name in cart:
        cart[item_name]["qty"] += 1 # 카트에 동일 상품이 있는 경우 수량만 증가 
    else:
        cart[item_name] = {"price":product["price"],"qty":1} # 카트에 없으면 최초등록 1개
        
    session["cart"] = cart  # 변수 cart를 세션 cart키에 값으로 저장 
    session.permanent = True # 5분 만료 적용 
    
    return redirect(url_for("show_cart")) # 카드에 저장 후 장바구니 보기로 이동 

# 장바구니 부분 삭제
@app.route("/remove/<item_name>")
def remove_to_cart(item_name):
    cart = session.get("cart")
    if item_name in cart:
        del cart[item_name]
    session["cart"] = cart
    return redirect(url_for("show_cart"))  # redirect는 클라이언트 요청을 부르는 것이기 때문에 홈페이지 리로드 된다.
    
@app.route("/clear")
def clear_cart():
    session.pop("cart",None)
    return redirect(url_for("show_cart"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
