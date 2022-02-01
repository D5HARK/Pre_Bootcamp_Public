import re
from flask_app.config.mysqlconnection import connecttoMySQL
from flask import flash, Flask
from flask_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_user(email):
        is_valid = True
        if not EMAIL_REGEX.match(email):
            flash("invalid email", "email err")
            is_valid = False
        return is_valid

    @staticmethod
    def check_password(password, s_password):
        is_valid = True
        if len(password) < 8:
            flash("Password must be 8 or more characters.", "pass err")
            is_valid = False
        if password != s_password:
            flash("Passwords must match.", "pass err")
            is_valid = False
        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connecttoMySQL("recipes_schema").query_db(query, data)
        return result

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connecttoMySQL("recipes_schema").query_db(query, data)
        if len(result) < 1:
            return False
        logged_user = []
        for user in result:
            logged_user.append(cls(user))
        return cls(result[0])
