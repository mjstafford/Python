from flask import flash
from app.config.mysqlconnection import connectToMySQL
from app import DATABASE,app
import re

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

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
    def save(cls, data):
        password_hashed = bcrypt.generate_password_hash(data["password"])
        data = {
            **data,
            "password": password_hashed
        }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def find_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        
        if len(result) == 0:
            return False

        user = User(result[0]) #returns an actual user instance!
        return user


    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data["first_name"]) < 2:
            flash("first name must be at least 2 characters", "register")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("last name must be at least 2 characters", "register")
            is_valid = False

        if not EMAIL_REGEX.match(data["email"]):
            flash("incorrect email format", "register")
            is_valid = False

        if data["password"] != data["password_confirm"]:
            flash("passwords didn't match", "register")
            is_valid = False

        if User.find_user_by_email({"email": data["email"]}):  #must only send email
            flash("user is already in system", "register")
            is_valid = False

        print("is valid:", is_valid)
        return is_valid


    @staticmethod
    def validate_login(data):
        is_valid = True

        user = User.find_user_by_email({"email": data["email"]})

        if not user:
            flash("Invalid user/password", "login")
            is_valid = False

        elif not bcrypt.check_password_hash(user.password, data["password"]):
            flash("Invalid user / password", "login")
            is_valid = False

        return is_valid

