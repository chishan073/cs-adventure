from flask import Flask # 引入 Flask 模組 flask 是一個輕量級的網頁框架
# 這行是用來引入 Flask 模組，讓我們可以使用 Flask 框架來建立網頁應用程式。
from functools import wraps # 引入裝飾器模組
# 這行是用來引入 functools 模組中的 wraps 函式，讓我們可以創建裝飾器。
# wraps 函式可以保留原函式的名稱、文件字串和其他屬性，這樣裝飾器就不會改變原函式的資訊。

app = Flask(__name__) # 建立 Flask 應用程式的實例
# __name__ 是 Python 的內建變數，代表當前模組的名稱。
# 當這個模組被直接執行時，__name__ 的值會是 "__main__"。
# 如果這個模組被其他模組導入，__name__ 的值會是模組的名稱。
# Flask 應用程式會根據這個名稱來決定應用程式的根目錄和資源路徑。
# 這行的意思是：建立一個 Flask 應用程式的實例，並將其命名為 app。
# 這個實例將會是我們整個網頁應用程式的核心，所有的路由、視圖函式和其他設定都會在這個實例上進行。
# 📍 首頁路由

# ✅ 自訂裝飾器：加上歡迎訊息
def add_greeting(func): # 定義裝飾器函式
    """
    裝飾器函式：在原函式的結果前加上歡迎訊息
    """
    @wraps(func)  # 保留原函式名稱與註解 func代表原函式
    def wrapper():
        original_result = func()
        return "👋 Welcome!\n" + original_result
    return wrapper

# 📍 套用裝飾器 + Flask 路由
@app.route("/")
@add_greeting
def home():
    return "This is the home page."

@app.route("/about")
@add_greeting
def about():
    return "This is the about page."

if __name__ == "__main__":
    app.run(debug=True)
