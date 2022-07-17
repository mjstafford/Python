from app import app, DATABASE
from flask import Flask, render_template, redirect, session, request
from app.models.user import User

@app.route("/users")
def users_page():
    #get users from model and render to page
    return render_template("users.html", users = User.find_all())

@app.route("/users/new", methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"]
    }
    User.save(data)
    return redirect("/users")

@app.route("/users/<int:user_id>")
def user_show_page(user_id):
    data = {"id": user_id}

    user = User.get_user_by_id(data)[0]     #returns list so had to get 0th index of it
    all_books = User.get_all_fav_books(data)

    return render_template("user_show.html", all_books = all_books, user = user)
