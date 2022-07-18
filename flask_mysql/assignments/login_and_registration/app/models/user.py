from flask import flash
from app.config.mysqlconnection import connectToMySQL
from app import DATABASE
import re

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-z0-9.+_-]+\.[a-zA-z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def find_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        #refactor suggestion (WOULD REQUIRE OTHER CHANGES IN OTHER LOGIC SINCE CURRENTLY OTHER LOGIC ALL DEPENDS ON RECIEVING A LIST)
            # return false if there are no users with that email
            # otherwise, instanciate object here & return that
        return connectToMySQL(DATABASE).query_db(query, data)   #this is currently the raw data

    @staticmethod
    def validate_user( user ):
        is_valid = True

        #first name
        if len(user["first_name"]) < 2:
            flash("first name must be at least 2 characters", "register")
            is_valid = False
        if not user["first_name"].isalpha():
            flash("first name must only be letters", "register")
            is_valid = False
        
        #last name
        if len(user["last_name"]) < 2:
            flash("last name must be at least 2 characters", "register")
            is_valid = False
        if not user["last_name"].isalpha():
            flash("last name must only be letters", "register")
            is_valid = False
        
        #email
        if not EMAIL_REGEX.match(user["email"]):
            flash("incorrect email format", "register")
            is_valid = False
        if len(User.find_by_email(user)) > 0:
            flash("user is already in system", "register")
            is_valid = False

        #password
        if len(user["password"]) < 8:
            flash("password must be at least 8 characters", "register")
            is_valid = False
        if not user["password"].isalnum():
            flash("password must contain atleast one number and one letter", "register")
            is_valid = False
        if not any(char.isupper() for char in user["password"]):
            flash("one upper case letter must exist!", "register")
            is_valid = False

        if user["password"] != user["confirm_password"]:
            flash("passwords didn't match", "register")
            is_valid = False

        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True

        results = User.find_by_email(data)

        if len(results) == 0:
            flash(f'No user associated with {data["email"]}', "login")
            is_valid = False

        return is_valid