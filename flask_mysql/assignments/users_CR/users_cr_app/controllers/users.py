#name file the plural of the model its for
from flask import Flask,render_template,redirect,request
from users_cr_app import app #app is in __init__.py
from users_cr_app.models.user import User

@app.route('/users')
def read():
    return render_template('read.html', all_users=User.get_all())


@app.route('/users/new')
def create():
    return render_template('create.html')

@app.route('/users/new/process_new', methods=['POST'])
def process_new_user():
    # call on model to save the new user and then send back to main page
    print("processing.... sending back to /users")
    return redirect('/users')