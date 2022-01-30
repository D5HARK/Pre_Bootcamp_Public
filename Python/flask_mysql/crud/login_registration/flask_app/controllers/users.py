from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_app.models.user import User
from flask_app import app





@app.route("/")
def show_home():
    return render_template("home.html")

@app.route("/create", methods=['POST'])
def create_user():
    data = {
        "first_name": request.form["f_name"],
        "last_name": request.form["l_name"],
        "email": request.form["email"],
        "password": request.form["password"]
    }
    if not User.check_password(request.form['password'], request.form['s_password']):
        return redirect('/')
    if not User.validate_user(request.form['email']):
        return redirect('/')
    
    User.save(data)
    return redirect("/")


@app.route("/dashboard")
def show_dash():
    return render_template("user_dash.html")