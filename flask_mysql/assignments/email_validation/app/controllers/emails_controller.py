from flask import Flask,render_template,session,flash,redirect,request
from app import app
from app.models.email import Email

@app.route("/")
def email_page():
    return render_template("email_form.html")

@app.route("/email/new", methods=["POST"])
def create_email():
    # check if email is valid, if not redirect back
    if not Email.is_valid_email(request.form):
        return redirect("/")
    # if it is valid, SAVE and then redirect to success with all emails shown
    data = {
        "email":request.form["email"]
    }
    print(Email.save(data))     #saves and then prints id in terminal
    return redirect("/success")

@app.route("/success")
def success_page():
    #get all emails and display
    return render_template("success.html", emails=Email.find_all())

@app.route("/delete/<int:id>")
def delete_email(id):
    data = {
        "id":id
    }
    Email.delete_by_id(data)
    return redirect("/success")
