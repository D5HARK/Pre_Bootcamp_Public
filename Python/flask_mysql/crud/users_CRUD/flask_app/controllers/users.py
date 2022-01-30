from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User




@app.route("/")
def index():
    users = User.get_all()
    return render_template("home.html", all_users=users)


@app.route("/new_user")
def newbie():
    return render_template("create.html")


@app.route("/create", methods=["POST"])
def handle_data():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    User.save(data)
    return redirect("/")

@app.route("/user/show/<user_id>")
def show_user(user_id):
    user = User.get_user(user_id)
    return render_template("user.html", profile=user)

@app.route("/user/edit/<user_id>")
def edit_page(user_id):
    user = User.get_user(user_id)
    return render_template("edit.html", profile=user)


@app.route("/edit/<user_id>", methods=["POST"])
def edit_data(user_id):
    new_data = {
        "new_f_name": request.form["first_name"],
        "new_l_name": request.form["last_name"],
        "id": user_id
    }
    User.edit_user(new_data)
    return redirect("/")

@app.route("/user/delete/<user_id>")
def delete_user(user_id):
    print("hello")
    User.delete({"id": user_id})
    return redirect("/")