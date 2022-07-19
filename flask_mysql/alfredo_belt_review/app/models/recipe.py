from app.config.mysqlconnection import connectToMySQL
from app import DATABASE

class Recipe:
    def __init__(self, data):   #includes every column for tables!
        self.id = data["id"]
        self.name = data["name"]
        self.under_thirty = data["under_thirty"]
        self.instructions = data["instructions"]
        self.date_made = data["date_made"]
        self.updated_at = data["updated_at"]
        self.created_at = data["created_at"]
        self.user_id = data["user_id"]

    @classmethod
    def find_all(cls):
        recipes = []

        query = "SELECT * FROM recipes LEFT JOIN users on users.id = user_id;"
        results = connectToMySQL(DATABASE).query_db(query)  

        if len(results) == 0:
            return False

        for recipe in results:
            # data = {
            #     **recipe,
            #     "user_id" = recipe["users.user_id"]
            # }
            print(recipe["id"], recipe["name"])

            # add a user to the class as an attribute before adding it to my list! That way every recipe containes the user that made it which then that info can be called in the view!
            recipes.append(cls(recipe))

        return recipes

