from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' #required for session, any password works

#sessions can only exist within a active HTTP request! cannot decale outside of that!

@app.route("/")
def home_page():
    if "visited" in session:
        print(f"you have visited {session['visited']} times!")
        session["visited"] = session["visited"] + 1
    else:
        session["visited"] = 1
    return render_template("index.html", count=session["visited"])

@app.route("/destroy_session")
def clear_session():
    session.clear()
    return redirect("/")

@app.route("/two")
def two_visits():
    if "visited" in session:
        print(f"you have visited {session['visited']} times!")
        session["visited"] = session["visited"] + 1
    else:
        session["visited"] = 1
    return redirect("/")

@app.route('/this_many', methods=['POST'])
def this_many_times():                  #can access info via request.form
    print(request.form)                 #which is a list of tuples! (See below)
    if "visited" in session:
        print(f"you have already visited {session['visited']} times!")
        session["visited"] = session["visited"] + int(request.form["number"]) - 1   #subtracting 1 because I always add one more with the redirect
    print(f"adding {session['visited']} more times!")
    return redirect('/')	

if __name__ == "__main__":
    app.run(debug=True)