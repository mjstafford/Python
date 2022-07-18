from app import app
from app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template, redirect, session, flash,request
from flask_bcrypt import Bcrypt
from app.models.user import User

bcrypt = Bcrypt(app)    #why do we add app?

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/new", methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect("/")        #returns with flashed messages

    password_hashed = bcrypt.generate_password_hash(request.form["password"])
    print(password_hashed)
    user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": password_hashed
    }

    id = User.save(user)
    session["user_id"] = id
    session["user_name"] = user["first_name"] + " " + user["last_name"]

    return redirect("/success")


@app.route("/success")
def successful_registration():
    if "user_id" not in session:
        return "You are not logged in! <a href='/'>Home</a>"
    return render_template("success.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    # validate
    if not User.validate_login(request.form):
        return redirect("/")        #returns with flashed messages
    
    user = User.find_by_email(request.form)[0]      #not a object yet
    user_instance = User( user )
    print('******************')
    print(user['password'])
    print(user_instance.first_name)
    print("$$$$$$$$$$$$$$$$$")
    
    if not bcrypt.check_password_hash(user["password"], request.form["password"]):
        flash("Invalid password", "login")
        return redirect("/")

    session["user_id"] = user_instance.id
    session["user_name"] = user_instance.first_name + " " + user_instance.last_name

    return redirect("/success")