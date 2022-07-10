from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "abc123"

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def post_page():
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

if __name__ == "__main__":
    app.run(debug=True)
