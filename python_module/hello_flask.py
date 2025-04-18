from flask import Flask

app = Flask(__name__)

# 首頁路由
@app.route("/") #當使用者輸入網址 訪往flask伺服器後 會執行這個函式
# @app.route("/<name>") #當使用者輸入網址 訪往flask伺服器後 會執行這個函式
def home():
    return "👋 Hello, Flask! 這是我的第一個網頁！"

# 關於我們路由
@app.route("/about")
def about():
    return "📖 這是關於我們的頁面。歡迎來到我的網站！"

if __name__ == "__main__":
    app.run(debug=True)

