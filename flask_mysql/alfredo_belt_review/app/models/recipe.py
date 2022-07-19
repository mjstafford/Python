from app.config.mysqlconnection import connectToMySQL
from flask import flash
from app import  DATABASE
from app.models.user import User

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.under_thirty = data["under_thirty"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_thirty, user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_thirty)s,%(user_id)s);"

        return connectToMySQL(DATABASE).query_db(query, data)   #returns an id

    @classmethod
    def get_all_recipes_with_users(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id"

        results = connectToMySQL(DATABASE).query_db(query) # list of dicts with all data from both tables

        #now we want to 
        list_recipes = []
        for row in results:
            current_recipe = cls(row)
            user_data = {                       
                **row,
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"],
                "id": row["users.id"]
            }

            current_user = User( user_data)         #user in that recipe
            current_recipe.user = current_user      #add instance attribute to this recipe of that user 
            list_recipes.append( current_recipe )   #append this instance into a list (of all other recipes with users attributes added)
        
        return list_recipes

    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id = users.id WHERE recipes.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data) # list of one result of the right id

        if len(results) > 0:
            current_recipe = cls( results[0])
            user_data = {                       
                **results[0],
                "created_at": results[0]["users.created_at"],
                "updated_at": results[0]["users.updated_at"],
                "id": results[0]["users.id"]
            }
            current_recipe.user = User(user_data)
            return current_recipe
        else:
            return None

    # @app.route("/recipes/<int:id>/update")
    # def display_updated_recipe(id):



    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if data["name"] == "":
            flash("Name must not be empty", "error_recipe_name")
            is_valid = False
        if data["description"] == "":
            flash("description must not be empty", "error_recipe_description")
            is_valid = False
        if data["instructions"] == "":
            flash("instructions must not be empty", "error_recipe_instructions")
            is_valid = False
        if data["date_made"] == "":
            flash("date made must not be empty", "error_recipe_date_made")
            is_valid = False
        if len(data["name"]) < 3:
            flash("name must be at least 3 chars long", "error_recipe_name")
            is_valid = False
        if len(data["description"]) < 3:
            flash("description must be at least 3 chars long", "error_recipe_description")
            is_valid = False
        if len(data["instructions"]) < 3:
            flash("instructions must be at least 3 chars long", "error_recipe_instructions")
            is_valid = False

        return is_valid