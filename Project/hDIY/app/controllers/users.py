from flask import Flask, session, flash, redirect, render_template, request
from app import app
from app.models.user import User
from app.models.blog import Blog
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#Landing page
@app.route("/")
def landing_page():
    return render_template("read.html")

#Landing page
@app.route("/register", methods=["POST"])
def register_page():
    #if not valid redirect to main page with flash
    if not User.validate_registration(request.form):
        return redirect("/")
    
    data = {
        **request.form,
        "password": bcrypt.generate_password_hash(request.form["password"])
    }
        
    id = User.save(data)

    session["user_id"] = id
    session["user_first_name"] = request.form["first_name"]
    session["user_last_name"] = request.form["last_name"]
    session["user_email"] = request.form["email"]

    return redirect("/home")

@app.route("/login", methods=["POST"])
def sign_in_page():
    if not User.validate_login(request.form):
        return redirect("/")

    #check if password matches db
    current_user = User.find_by_email(request.form)
    if not bcrypt.check_password_hash(current_user.password, request.form["password"]):
        flash("Wrong credientials", "password_login_error")
        return redirect("/")

    session["user_id"] = current_user.id
    session["user_first_name"] = current_user.first_name
    session["user_last_name"] = current_user.last_name
    session["user_email"] = current_user.email

    return redirect("/home")

@app.route("/logout")
def log_user_out():
    session.clear()
    return redirect("/")

@app.route("/home")
def home_page():
    #clear form data if user leaves to homepage
    if "title" in session or "description" in session:
        session.pop("title")
        session.pop("description")

    if "user_first_name" in session:
        recent_blogs = Blog.sort_by_date()
        favorite_blogs = Blog.find_all_favorites_of_user({"user_id":session["user_id"]})
        # print("HERRRRRRRRRRRRRRRRRRRRRRRRRERASDF ASDFASDF ASD FA SDDF\n\n",favorite_blogs)
        return render_template("home.html", recent_blogs=recent_blogs, favorite_blogs=favorite_blogs)
    return redirect("/")

@app.route("/home/<string:filter>")
def home_page_filtered(filter):
    if "user_first_name" in session:
        recent_blogs = Blog.sort_by_date()
        favorite_blogs = Blog.find_all_favorites_of_user({"user_id":session["user_id"]})

        data = {
            "name" : filter
        }
        filtered_results = Blog.find_by_category(data)

        return render_template("home.html", filtered_blogs=filtered_results, recent_blogs=recent_blogs, favorite_blogs=favorite_blogs)
    return redirect("/")
