import os
from flask import Flask, render_template, session, request, redirect, flash, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "abc123"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/process", methods=["POST", "GET"])
def post_page():
    #first validate
    print(request.form)
    print(request.files)
    if not validate_form(request.form):
        return redirect("/")

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # return redirect(url_for('download_file', name=filename))

    session["name"]= request.form["name"]
    session["dojo location"]= request.form["location"]
    session["favorite language"]= request.form["language"]
    session["comment"]= request.form["comment"]

    print(request.form)
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
