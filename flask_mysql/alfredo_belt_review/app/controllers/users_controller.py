from app import app
from flask import render_template, request, redirect,flash, session
from app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def display_login():
    return render_template("index.html")

@app.route("/user/registration", methods=["POST"])
def process_registration():
    #validate the registration form
    if User.validate_registration (request.form) == False:
        return redirect("/")

    #validate if user already exists
    user_exists = User.get_one_to_validate_email(request.form)
    print(user_exists)
    if user_exists != None:
        flash("This email already exists!", "email_error")
        return redirect("/")
    
    data = {
        **request.form,     #this deep copies one dict to this one
        "password": bcrypt.generate_password_hash(request.form["password"])        # override anything we need to
    }
    print(data)

    #if new user, create the user via SAVE method
    user_id = User.create( data )                 # <this data dict has hashed password

    session["first_name"] = data["first_name"]
    session["email"] = data["email"]
    session["id"] = user_id
    
    return redirect("/recipes")

@app.route("/user/login", methods=["POST"])
def process_login():
    current_user = User.get_one_to_validate_email(request.form)
    if current_user != None:
        if not bcrypt.check_password_hash(current_user.password, request.form["password"]):
            flash("Wrong credientials", "password_login_error")
            return redirect("/")

        session["first_name"] = current_user.first_name
        session["email"] = current_user.email
        session["id"] = current_user.id

        return redirect("/recipes")
    else:
        flash("Wrong credientials", "password_login_error")
        return redirect("/")

