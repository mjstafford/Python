from flask import Flask, render_template, redirect, session, request, url_for
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' #required for session, any password works

@app.route("/")
def main_page():
    if request.args:
        guessed_number = int(request.args.get("guessed_number"))
        print(int(guessed_number))
        print(type(guessed_number))
    else:
        guessed_number = ""
    if 'secret_number' not in session:
        session["secret_number"] = random.randint(1,100)
    print(session["secret_number"] )
    print(type(session["secret_number"]) )
    return render_template("index.html", secret_number=session["secret_number"], guessed_number=guessed_number )

@app.route("/guess", methods=["POST"])
def guess_post_route():
    print(request.form["num"])
    return redirect(url_for("main_page", guessed_number=request.form["num"]))

if __name__ == "__main__":
    app.run(debug=True)