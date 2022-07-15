#needs more things
from app import app
from app.controllers import dojos_controller
from app.controllers import ninjas_controller

if __name__ == "__main__":
    app.run(debug=True)