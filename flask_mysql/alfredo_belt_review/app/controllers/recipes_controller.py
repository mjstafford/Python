from app import app
from flask import render_template, request, redirect,flash, session
from app.models.recipe import Recipe

@app.route("/recipes")
def display_recipes():
    if "email" not in session:  #if user was created or loged in, they get in if not... redirect!
        return redirect ("/")
    list_recipes = Recipe.get_all_recipes_with_users()
    return render_template("recipes.html", list_recipes = list_recipes)

@app.route("/display/recipe/create")
def display_create_recipe():
    return render_template("create_recipe.html")

@app.route("/recipe/create", methods=["POST"])
def create_recipe():
    #validate fields
    if Recipe.validate_recipe(request.form) == False:
        return redirect("/display/recipe/create")

    #if valid, create recipe
    data = {
        **request.form,
        "user_id": session["id"]       #required to make a Recipe, and not in our form!
    }

    Recipe.create(data)
    #redirect to the /recipes
    
    return redirect("/recipes")

@app.route("/recipes/<int:id>")
def display_one(id):
    if "email" not in session:
        return redirect("/")
    data = {"id": id}
    current_recipe = Recipe.get_one_with_user(data)
    return render_template("recipe.html", current_recipe=current_recipe)