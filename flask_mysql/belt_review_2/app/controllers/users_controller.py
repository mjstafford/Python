from app import app
from flask import Flask, redirect, render_template, request, session, flash
from app.models.user import User

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#main page
@app.route("/")
def main_page():
    return render_template("index.html")

#login page
@app.route("/login", methods=["POST"])
def login_process():
    current_user = User.validate_user_login(request.form)
    if current_user != None:
        if not bcrypt.check_password_hash(current_user.password, request.form["password"]):
            flash("Wrong credientials", "password_login_error")
            return redirect("/")

        session["user_name"] = current_user.first_name
        session["email"] = current_user.email
        session["user_id"] = current_user.id

        return redirect("/recipes")
    else:
        flash("Wrong credientials", "password_login_error")
        return redirect("/")


#register page
@app.route("/user/register", methods=["POST"])
def process_registration():
    #validate form data
    if not User.validate_user(request.form):
        return redirect ("/")

    #if correct, make sure user not in db
    current_user = User.find_by_email(request.form)

    #if current_user == None, that means there are no users with that email already, so we can go ahead and create one!
    if current_user == None:
        #save user and send to '/recipes/
        user_id = User.save(request.form)

        #add session info!
        session["user_id"] = user_id
        session["user_name"] = request.form["first_name"]
        session["email"] = request.form["email"]

        return redirect("/recipes")
    else:
        flash("user already exists!", "email_error")
        return redirect("/")


@app.route("/logout")
def log_user_out():
    session.clear()
    return redirect("/")