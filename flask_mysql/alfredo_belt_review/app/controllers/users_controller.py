from flask import Flask, redirect, render_template, session, flash, request
from app import app
from app.models import user

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/user/new", methods=["POST"])
def create_user():
    is_valid_user = user.User.validate_user(request.form)
    print("is valid user",is_valid_user)
    if not is_valid_user:
        redirect("/")
    
    #if everything is good, save the user!
    id = user.User.save(request.form)
    
    session["user_id"] = id
    session["user_first_name"] = request.form["first_name"]
    return redirect("/recipes")    #change to recipes page

@app.route("/login", methods=["POST"])
def login_user():
    is_valid_login = user.User.validate_login(request.form)
    print("is valid login", is_valid_login)
    if not is_valid_login:
        redirect("/")
    
    my_user = user.User.find_user_by_email({"email": request.form["email"]})

    session["user_id"] = my_user.id
    session["user_first_name"] = my_user.first_name

    return redirect("/recipes")

@app.route("/logout")
def logout():
    session.clear()
    return render_template("index.html")