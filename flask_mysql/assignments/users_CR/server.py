# we 100% need the first import because it basically injects all the routes back into this file
from users_cr_app.controllers import users #this imports the users controller!
from users_cr_app import app    #this is because of the __init__ file under users_cr_app

if __name__== "__main__":
    app.run(debug=True)