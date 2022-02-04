from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_app.models.user import User
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/")
def show_home():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    data = {"email": request.form['log_email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("No account with this email exists")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['log_password']):
        flash("invalid email/password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route("/create", methods=['POST'])
def create_user():
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["f_name"],
        "last_name": request.form["l_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    if not User.check_password(request.form['password'], request.form['s_password']):
        return redirect('/')
    if not User.validate_user(request.form['email']):
        return redirect('/')
    if not User.name_length(request.form['f_name'], request.form['l_name']):
        return redirect('/')

    user_id = User.save(data)
    flash("account created, please log in")
    session['user_id'] = user_id
    return redirect("/")

@app.route("/user/edit/<user_id>")
def user_edit_page(user_id):
    item = User.get_user(user_id)
    return render_template("edit_account.html", user=item)

@app.route("/logout", methods = ["POST"])
def end_session():
    session.clear()
    return redirect('/')

