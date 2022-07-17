from flask import flash
from app import DATABASE
from app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-z0-9.+_-]+\.[a-zA-z]+$')

class Email:
    def __init__(self, email_data):
        self.id = email_data["id"]
        self.email = email_data["email"]
        self.created_at = email_data["created_at"]
        self.updated_at = email_data["updated_at"]
    
    @classmethod
    def find_all(cls):
        all_emails = []
        query = "SELECT * FROM emails;"
        emails_raw_data = connectToMySQL(DATABASE).query_db(query)
        for email in emails_raw_data:
            all_emails.append(cls(email))
        return all_emails

    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_by_id(cls, data):
        query = "DELETE FROM emails WHERE emails.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def is_valid_email(email_data):
        is_valid = True
        if not EMAIL_REGEX.match(email_data["email"]):
            flash("Email is not valid!")
            is_valid = False

        #query db to check if name in db
        query = "SELECT * FROM emails WHERE email=%(email)s"
        result = connectToMySQL(DATABASE).query_db(query, email_data)       #does this data need to be a class?
        if len(result) > 0:
            flash(f"{email_data['email']} already exists in the db")
            is_valid = False

        if is_valid:
            flash(f"The email address you entered ({email_data['email']}) is a VALID email address! Thank you!")
        return is_valid
