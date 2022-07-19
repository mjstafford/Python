from app.config.mysqlconnection import connectToMySQL
from flask import flash
from app import EMAIL_REGEX, DATABASE

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
    def get_one_to_validate_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data) #raw data

        if len(result) > 0:     #check to see if there are results
            current_user = cls(result[0])
            return current_user

        return None

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        result_id = connectToMySQL(DATABASE).query_db(query, data)
        return result_id

    @staticmethod
    def validate_registration(data):
        is_valid = True

        if len(data["first_name"]) < 2:
             flash("Your first name needs to have at least 2 chars", "first_name_error")
             is_valid = False

        if len(data["last_name"]) < 2:
             flash("Your last name needs to have at least 2 chars", "last_name_error")
             is_valid = False

        if not EMAIL_REGEX.match(data["email"]):
             flash("Invalid email", "email_error")
             is_valid = False

        if data["password"] != data["password_confirm"]:
             flash("passwords do not match", "password_error")
             is_valid = False

        return is_valid

