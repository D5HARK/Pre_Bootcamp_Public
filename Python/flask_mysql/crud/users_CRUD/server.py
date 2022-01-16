import re
from flask import Flask, render_template, request, redirect, session
from user import User

app = Flask(__name__)
app.secret_key = "0V*x4+Imm4(Uy0I+kO0$fR0_"


@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("home.html", all_users=users)

@app.route("/new_user")
def newbie():
    return render_template("create.html")

@app.route("/create", methods = ["POST"])
def handle_data():
    data = {
        "first_name": request.form["first_name"],
        "last_namme": request.form["last_name"]
    }
    User.save(data)
    return redirect("/")
if __name__ == "__main__":
    
    app.run(debug=True, port=8080)
