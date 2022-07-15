from flask import Flask, render_template, redirect, request
from app import app
from app.models.dojo import Dojo

@app.route("/dojos")
def dojo_page():
    all_dojos = []
    dojos_result =  Dojo.find_all() #returns a list of objects (not classes)
    for dojo in dojos_result:
        all_dojos.append(Dojo(dojo))
    return render_template('dojo.html', dojos=all_dojos)