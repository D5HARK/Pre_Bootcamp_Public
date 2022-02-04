from flask import Flask, flash, redirect, render_template, request, url_for, session
from flask_app.models.magazine import Magazine
from flask_app import app

@app.route("/dashboard")
def dash():
    magazines = Magazine.get_all()
    return render_template("dash.html", all_magazines=magazines)

@app.route("/new_magazine")
def new_recipe_page():
    return render_template("new_magazine.html")

@app.route("/create_magazine", methods=['POST'])
def create_magazine():
    data = {
        "title": request.form["title"],
        "description": request.form["description"],   
    }
    Magazine.save(data)
    return redirect("/dashboard")

@app.route("/magazine/show/<magazine_id>")
def show_magazine(magazine_id):
    item = Magazine.get_magazine(magazine_id)
    return render_template("magazine.html", magazine=item)

@app.route("/magazine/edit/<magazine_id>")
def magazine_edit_page(magazine_id):
    item = Magazine.get_magazine(magazine_id)
    return render_template("edit_magazine.html", magazine=item)
