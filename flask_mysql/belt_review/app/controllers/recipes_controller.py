from flask import Flask, redirect, render_template, session, flash, request
from app import app
from app.models import recipe

@app.route("/recipes")
def recipes_page():
    #first validate that the user is logged in

    #next return all the lists of todos
    return render_template("recipes.html", recipes = recipe.Recipe.find_all())