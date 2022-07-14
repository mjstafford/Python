#do we need this first import!?
from users_cr_app.controllers import users #this imports the users controller!
from users_cr_app import app

if __name__== "__main__":
    app.run(debug=True)