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
    categories = ["kitchen", "bathroom", "plumbing", "electrical", "yard"]

    if not Blog.validate_blog(request.form):
        session["title"] = request.form["title"]
        session["description"] = request.form["description"]
        print(request.form)
        return redirect("/blog/new")

    #else, save the blog & then save the blog id to the ALL categories selected
    blog_data = {
        **request.form,
        "user_id": session["user_id"]
    }
    id = Blog.save(blog_data)

    for category in categories:
        if category in request.form:
            data = {
                "categories_id" : request.form[category],
                "blogs_id" : id
            }
            Category.save(data)
    

    return redirect('/home')

