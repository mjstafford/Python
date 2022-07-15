from flask import Flask, render_template, redirect, request
from app import app
from app.models.dojo import Dojo
from app.models.ninja import Ninja

@app.route("/dojos")
def dojo_page():
    all_dojos = []
    dojos_result =  Dojo.find_all() #returns a list of objects (not classes)
    for dojo in dojos_result:
        all_dojos.append(Dojo(dojo))
    return render_template('dojo.html', dojos=all_dojos)

@app.route("/dojos/<int:id>")
def dojo_show_page(id):
    all_ninjas = []
    ninjas_result =  Dojo.find_ninjas_at_dojo(id) 
    dojo_name = ninjas_result[0]["name"]
    # print(ninjas_result)
    # print(dojo_name)
    for ninja in ninjas_result:
        all_ninjas.append(Ninja(ninja))

    return render_template('dojo_show.html', ninjas=all_ninjas, dojo_name = dojo_name)
#example of data returnedfrom ninjas_result
# [
    # {'id': 1, 
    # 'name': 'Cobra Kai', 
    # 'created_at': datetime.datetime(2022, 7, 13, 7, 59, 46), 
    # 'updated_at': datetime.datetime(2022, 7, 13, 7, 59, 46), 
    # 'ninjas.id': 1, 
    # 'first_name': 'Johnny', 
    # 'last_name': 'Lawrence', 
    # 'age': 55, 
    # 'ninjas.created_at': datetime.datetime(2022, 7, 13, 7, 59, 46), 
    # 'ninjas.updated_at': datetime.datetime(2022, 7, 13, 7, 59, 46), 
    # 'dojo_id': 1
    # }, 
    # {}, {}, ...
# ]

