from app import app
from flask import Flask, redirect, render_template, request, session, flash
from app.models.recipe import Recipe

#recipes page
@app.route("/recipes")
def recipes_page():
    if "email" not in session:
        return redirect("/")
    return render_template("recipes.html", recipes=Recipe.find_all_recipes())

#create recipes page
@app.route("/recipes/new")
def recipes_form_page():
    if "email" not in session:
        return redirect("/")
    return render_template("recipes_form.html")

@app.route("/recipes/process", methods=["POST"])
def recipes_processing():
    if "email" not in session:
        return redirect("/")
    #if not valid, redirect to page with flashed messages
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    
    #if valid save the recipe
    Recipe.save(request.form)

    return redirect("/recipes")


@app.route("/recipes/update/<int:id>", methods=["POST"])
def recipes_process_update(id):
    if "email" not in session:
        return redirect("/")
    #if not valid, redirect to page with flashed messages
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{id}")
    #if valid save the recipe 
    data = {
        **request.form,
        "id": id
    }
    Recipe.update(data)

    return redirect("/recipes")


#show single recipe
@app.route("/recipes/<int:id>")
def show_recipe(id):
    if "email" not in session:
        return redirect("/")
    data = {"id": id}
    #get recipe instance using id
    current_recipe = Recipe.find_by_id(data)

    if current_recipe == None:
        print("!!!!!!!!!!!!!!!!!! ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        return render_template("recipe_show.html", recipe=current_recipe)

@app.route("/recipes/edit/<int:id>")
def update_recipe_form(id):
    if "email" not in session:
        return redirect("/")
    data = {"id": id}
    #get recipe instance using id
    current_recipe = Recipe.find_by_id(data)

    return render_template("recipe_update.html", recipe=current_recipe)

@app.route('/delete/<int:id>')
def delete_processing(id):
    if "email" not in session:
        return redirect("/")
    Recipe.delete({"id":id})
    return redirect("/recipes")