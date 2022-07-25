from flask import flash, session
from app import DATABASE, EMAIL_REGEX, app
from app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.city = data["city"]
        self.state = data["state"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def find_by_email( cls, user_data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, user_data)
        print(result)

        if len(result) > 0:
            # create & return instance
            current_user = User( result[0] )
            return current_user
        else:
            return None

    @classmethod
    def save(cls, user_data):
        query = "INSERT INTO users (first_name, last_name, email, city, state, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(city)s,%(state)s,%(password)s);"
        id = connectToMySQL(DATABASE).query_db(query, user_data)
        return id

    @staticmethod
    def validate_registration( data ):
        is_valid = True
        
        #form checks
        if data["first_name"] == "":
            flash("first name cannot be blank", "first_name_error")
            is_valid = False
        elif len(data["first_name"]) < 2:
            flash("first name needs to have at least 2 chars", "first_name_error")
            is_valid = False

        if data["last_name"] == "":
            flash("last name cannot be blank", "last_name_error")
            is_valid = False
        elif len(data["last_name"]) < 2:
            flash("last name needs to have at least 2 chars", "last_name_error")
            is_valid = False

        if data["email"] == "":
            flash("email cannot be blank", "email_error")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email format", "email_error")
            is_valid = False

        if data["city"] == "":
            flash("City cannot be blank", "city_error")
            is_valid = False
        elif len(data["city"]) < 2:
            flash("City  needs to have at least 2 chars", "city_error")
            is_valid = False

        if "state" not in data:
            flash("State cannot be blank", "state_error")
            is_valid = False
        elif len(data["state"]) < 2:
            flash("State  needs to have at least 2 chars", "state_error")
            is_valid = False

        if data["password"] == "":
            flash("password cannot be blank", "password_error")
            is_valid = False
        elif len(data["password"]) < 8:
            flash("password needs to have at least 8 chars", "password_error")
            is_valid = False
        elif data["password"] != data["password_confirm"]:
            flash("passwords do not match", "password_error")
            is_valid = False

        #check for user 
        current_user = User.find_by_email(data)
        if current_user != None:    #then user exists
            flash("account already exists", "email_error")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        result = User.find_by_email(data)

        if data["email"] == "":
            flash("email cannot be blank", "email_login_error")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email format", "email_login_error")
            is_valid = False
        elif result == None:     #check to see if there are results
            flash("Invalid email/password", "email_login_error")
            is_valid = False

        if data["password"] == "":
            flash("password cannot be blank", "password_login_error")
            is_valid = False
        elif len(data["password"]) < 8:
            flash("password needs to have at least 8 chars", "password_login_error")
            is_valid = False

        return is_valid
