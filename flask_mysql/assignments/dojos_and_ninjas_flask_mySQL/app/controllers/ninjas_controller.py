from flask import Flask, render_template, redirect, request
from app import app
from app.models.dojo import Dojo
from app.models.ninja import Ninja

@app.route("/ninjas")
def ninjas_page():
    #sending dojos so that I can populate the dropdown menu for dojos
    return render_template('ninja.html', dojos = Dojo.find_all())

# incoming post data from form
@app.route("/ninja/new", methods=["POST"])
def create_ninja():
    #process incoming request.form data
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]    #the form shows a name but the value is an id!
    }

    #call save method to persist the ninja data to the db
    #sending save but also saving the return value which is the id
    new_ninja_id = Ninja.save(data)
    print(new_ninja_id)
    return redirect(f"/dojos/{request.form['dojo_id']}")
