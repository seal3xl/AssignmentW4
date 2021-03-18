from flask import Flask,render_template,request,redirect,session

app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #Secret Key

userData=[{"ac":"test","ps":"test"}]#將帳號密碼組放入userData，清單已用來驗證使用者輸入的帳號密碼。

#首頁
@app.route("/")
def index():
    return render_template("index.html")

#登入連線：輸入帳號密碼，如果與userData的資料吻合，將使用者記錄到session，並登入到member頁面。（登入失敗轉到登入失敗頁面。）
@app.route("/signin",methods=["POST"])
def signin():
    ac=request.form["ac"]
    ps=request.form["ps"]
    userIdentify={"ac":ac,"ps":ps}
    if userIdentify in userData:
        session["ac"]=request.form["ac"]
        return redirect("/member")
    else:
        return redirect("/error")

#會員頁面：先檢查使用者是否有在session裡面，有就帶出member頁面，沒有就轉到登入失敗頁面。
@app.route("/member")
def member():
    if "ac" in session:
        return render_template("member.html")
    else:
        return redirect("/howdare")

#登入失敗頁面
@app.route("/error")
def error():
    return render_template("error.html")

#登出：將使用者從session中移除，並導入首頁。
@app.route("/signout")
def signout():
    session.pop("ac",None)
    return redirect("/")

#登入失敗頁面2
@app.route("/howdare")
def howdare():
        return render_template("howdare.html")


app.run(port=3000)