from flask import Flask, render_template, redirect, request, session
from random import randint

app=Flask(__name__)
app.secret_key = "mybadkey"

money_dictionary = {
    "farm": lambda : randint(10,20),
    "cave": lambda : randint(5,10),
    "house": lambda : randint(2,5),
    "casino": lambda : randint(-50,50),
}
building_dictionary = {
    "Farm": "(earns 10-20 golds)",
    "Cave": "(earns 5-10 golds)",
    "House": "(earns 2-5 golds)",
    "Casino": "(earns/takes 0-50 golds)",
}

@app.route("/")
def main_page():
    #logic
    if "total" not in session:
        session["total"] = 0
    if "total" in session and "value change" in session:
        session["total"] += session["value change"]
        session.pop("value change")                 #without this on refresh it keeps adding the gold amount
    return render_template('index.html', building_dictionary= building_dictionary, total=session["total"])

@app.route("/process_money", methods=["POST"])
def process_money():
    building = request.form["building"]
    amount =  money_dictionary[building]()          # returns and calls the lambda function for rand int.
    session["value change"] = amount                # still an int when stored in session
    if "activities" not in session:
        session["activities"] = determine_message(amount, building)
    else:
        session["activities"] = determine_message(amount, building) + session["activities"]
    return redirect("/")

@app.route("/clear", methods=["POST"])
def clear_money():
    session.clear() 
    return redirect("/")

# helper function
def determine_message(amount, building):
        if amount > 0 :
            return f"<p class='green'>Earned {amount} golds from the {building}!</p>"
        if amount == 0:
            return f"<p>Entered a {building} and broke even... won {amount} golds</p>"
        else:    
            return f"<p class='red'>Entered a {building} and lost {amount} golds...ouch!</p>"

if __name__ == "__main__":
    app.run(debug=True)
