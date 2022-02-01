from flask import render_template, render_template_string, request, redirect, session
from flask_app import app
from flask_app.models.recipe import Recipe



@app.route("/dashboard")
def dash():
    recipes = Recipe.get_all()
    return render_template("dashboard.html", all_recipes=recipes)

@app.route("/new_recipe")
def new_recipe_page():
    return render_template("new_recipe.html")

@app.route("/create_recipe", methods=['POST'])
def create_recipe():
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "30_min": request.form["30_min"]
    }
    Recipe.save(data)
    return redirect("/dashboard")

@app.route("/recipe/show/<recipe_id>")
def show_recipe(recipe_id):
    food = Recipe.get_recipe(recipe_id)
    return render_template("recipe.html", recipe=food)


@app.route("/recipe/edit/<recipe_id>")
def recipe_edit_page(recipe_id):
    food = Recipe.get_recipe(recipe_id)
    return render_template("edit_recipe.html", recipe=food)

@app.route("/edit/recipe/<recipe_id>")
def edit_recipe(recipe_id):
    Recipe.get_all(recipe_id)
    new_data = {
        "new_name": request.form["name"],
        "new_description": request.form["description"],
        "new_instructions": request.form["instructions"],
        "new_date": request.form["date_made"],
        "new_30": request.form["30_min"],
        "id": recipe_id
    }
    Recipe.edit_recipe(new_data)
    return redirect("/recipe/show/<recipe_id>")


@app.route("/recipe/delete/<recipe_id>")
def delete_recipe(recipe_id):
    Recipe.delete({"id": recipe_id})
    return redirect("/dashboard")


