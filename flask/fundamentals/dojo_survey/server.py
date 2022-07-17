from flask import Flask, render_template, session, request, redirect, flash

app = Flask(__name__)
app.secret_key = "abc123"

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def post_page():
    #first validate
    if not validate_form(request.form):
        return redirect("/")

    session["name"]= request.form["name"]
    session["dojo location"]= request.form["location"]
    session["favorite language"]= request.form["language"]
    session["comment"]= request.form["comment"]
    return redirect("/result")

@app.route("/result")
def result_page():
    return render_template("result.html")

@app.route("/clear", methods=["POST"])
def go_back():
    session.clear()
    return redirect("/")

def validate_form(data):
    is_valid = True
    if len(data["name"]) <= 3:
        flash("Name must be at least 3 chars long")
        is_valid = False
    if  0 < len(data["comment"]) < 3:
        flash("comment must be at least 3 chars long")
        is_valid = False
    if "location" not in data:
        flash("must select a location")
        is_valid = False
    if "language" not in data:
        flash("must select a language")
        is_valid = False
    return is_valid

if __name__ == "__main__":
    app.run(debug=True)
