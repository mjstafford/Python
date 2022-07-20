from flask import flash, session
from app import DATABASE
from app.config.mysqlconnection import connectToMySQL
from app.models.user import User

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.under_thirty = data["under_thirty"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def find_all_recipes(cls):
        #need to add a user to each recipe!
        query = "SELECT * FROM recipes JOIN users WHERE users.id = user_id;"
        recipes_data = connectToMySQL(DATABASE).query_db(query)

        if len(recipes_data) == 0:
            return None
        else:
            #process list
            all_recipes = []

            for recipe in recipes_data:
                current_recipe = Recipe(recipe)

                #create the user and then add them as Instance attribute
                user_data = {
                    **recipe,
                    "id": recipe["users.id"],
                    "created_at": recipe["users.created_at"],
                    "updated_at": recipe["users.updated_at"]
                }
                print(user_data)
                current_user = User (user_data)
                current_recipe.user = current_user
                all_recipes.append(current_recipe)
            
            return all_recipes

    @classmethod
    def find_by_id(cls, recipe_id):
        #need to add a user to the single recipe!
        query = "SELECT * FROM recipes JOIN users WHERE users.id = user_id AND recipes.id = %(id)s;"
        recipe_data = connectToMySQL(DATABASE).query_db(query, recipe_id)

        if len(recipe_data) == 0:
            return None
        else:
            recipe = Recipe(recipe_data[0])

            #create the user and then add them as Instance attribute
            user_data = {
                **recipe_data[0],
                "id": recipe_data[0]["users.id"],
                "created_at": recipe_data[0]["users.created_at"],
                "updated_at": recipe_data[0]["users.updated_at"]
            }
            current_user = User (user_data)
            recipe.user = current_user
            
            return recipe

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE recipes.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def save(cls, recipe_data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, under_thirty, user_id) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_thirty)s, %(user_id)s);"

        #add user_id into the mix (since its requrired!)
        print("userid", session["user_id"])
        recipe_data_with_user_id = {
            **recipe_data,
            "user_id": session["user_id"]
        }

        id = connectToMySQL(DATABASE).query_db(query, recipe_data_with_user_id)
        return id

    @classmethod
    def update(cls, recipe_data):
        #ALWAYS HAVE A WHERE CLAUSE
        query = "UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_made=%(date_made)s, under_thirty=%(under_thirty)s WHERE recipes.id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, recipe_data)


    @staticmethod
    def validate_recipe(recipe_data):
        is_valid = True
        
        if len(recipe_data["name"]) < 3:
             flash("name must be at least 3 chars", "name_error_recipe")
             is_valid = False

        if len(recipe_data["description"]) < 3:
             flash("description must be at least 3 chars", "description_error_recipe")
             is_valid = False

        if len(recipe_data["instructions"]) < 3:
             flash("instructions must be at least 3 chars", "instructions_error_recipe")
             is_valid = False
        
        #should nest the above ones under these
        if recipe_data["name"] == "":
             flash("name is required", "name_error_recipe")
             is_valid = False

        if recipe_data["description"] == "":
             flash("description is required", "description_error_recipe")
             is_valid = False

        if recipe_data["instructions"] == "":
             flash("instructions is required", "instructions_error_recipe")
             is_valid = False
        
        if recipe_data["date_made"] == "":
             flash("date required", "date_made_error_recipe")
             is_valid = False


        return is_valid

