from flask import Flask, session, flash, redirect, render_template, request
from app import app
from app.models.user import User
from app.models.blog import Blog
from app.models.category import Category
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/blog/filter", methods=["POST"])
def process_category_filter():
    return redirect(f"/home/{request.form['filter']}")

@app.route("/blog/new")
def new_blog_form():
    # session.pop("title")
    # session.pop("description")
    # session.pop("cat_id")
    return render_template("blog_form.html", categories = Category.find_all())

@app.route("/blog/new/process", methods=["POST"])
def process_new_blog():
    
    if not Blog.validate_blog(request.form):
        session["title"] = request.form["title"]
        session["description"] = request.form["description"]
        session["cat_id"] = request.form["category"]
        print(request.form["category"])
        return redirect("/blog/new")

    return redirect('/home')

