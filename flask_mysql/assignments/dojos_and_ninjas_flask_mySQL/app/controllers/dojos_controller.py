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
    # print(ninjas_result)

    #should have an if statement to double check if any results exist before the next line
    dojo_name = ninjas_result[0]["name"]     #this returns a record which i can access the dojo name from. would break with 0 ninjas at dojo.
    # print(dojo_name)
   
    for ninja in ninjas_result:
        # keep in mind the returned data pre-fixed some columns like id with the table name id (is users id) therefore the other id is ninjas.id
        #therefore we must re-create the data in the way that the constructor of the Ninja class expects it (id vs ninjas.id)
        ninja_data = {
            "id": ninja['ninjas.id'],
            "first_name" : ninja["first_name"],      #unique column name therefore not prefix added
            "last_name" : ninja["last_name"],        #unique column name therefore not prefix added
            "age" : ninja["age"],                    #unique column name therefore not prefix added
            "created_at" : ninja["ninjas.created_at"],
            "updated_at" : ninja["ninjas.updated_at"]
        }
        all_ninjas.append(Ninja(ninja_data))
        
    #this will set the dojo instance variable ninjas(list of Ninjas) allowing us to just send the dojo object to html because this will hold all info needed!
    current_dojo = Dojo( ninjas_result[0] )
    current_dojo.ninjas = all_ninjas
    print(current_dojo)

    # return render_template('dojo_show.html', ninjas=all_ninjas, dojo_name = dojo_name)    #instead just sent dojo with list of ninjas in its instance variable 
                                                                                            # also updated html to use the following return statement
    return render_template('dojo_show.html', current_dojo = current_dojo)
#example of data returnedfrom ninjas_result
# [
    # {
        # 'id': 1, 
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
    # },
    # {k:v, etc...},
    # {k:v, etc...}
# ]

