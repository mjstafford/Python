import flask from Flask, session

app=Flask(__name__)
app.secret_key = "123"

DATABASE = "login_and_registration"