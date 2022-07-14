#name file the plural of the model its for
from flask import Flask,render_template,redirect,request
from users_cr_app import app #app is in __init__.py
from users_cr_app.models.user import User

@app.route('/users')
def read():
    return render_template('read.html', all_users=User.get_all(), count=0)


@app.route('/users/new')
def create():
    return render_template('create.html')

@app.route('/users/new/process_new', methods=['POST'])
def process_new_user():
    # save the data from the form into a dictionary
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    # call on model to save the new user and then send back to main page
    User.save(data)
    print("processing.... trying to save in route")
    return redirect('/users')

@app.route('/users/<int:id>')   #sets up url variable
def get_by_id(id):              #takes in that variable
    data = {                    # saves in a dict
        "id": id
    }
    return render_template('show.html', user=User.get_by_id(data)) #render show.html with data processed

@app.route('/delete/<int:id>')  #if this route is entered it will delete the id from the db
def delete_by_id(id):           #takes in id from url params
    data = { 'id': id }         #adds id into dict
    User.delete_by_id(data)     #calls on the delete_by_id method in the MODEL to send a query to delete provided id
    return redirect("/users")   #redirects to show all page

@app.route('/edit_page/<int:id>')
def edit_page(id):
    data = {
        'id': id
    }
    return render_template("update.html", user = User.get_by_id(data))

@app.route('/update/<int:id>', methods=["POST"])
def edit_by_id(id):
    data = { 
        'id': id, 
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update_by_id(data)
    return redirect(f"/users/{id}")
