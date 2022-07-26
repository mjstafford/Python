from flask import Flask, session, flash, redirect, render_template, request
from app import app
from app.models.user import User
from app.models.blog import Blog
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/blog/filter", methods=["POST"])
def process_category_filter():
    return redirect(f"/home/{request.form['filter']}")