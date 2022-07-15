from app.config.mysqlconnection import connectToMySQL

DATABASE = "dojos_and_ninjas_schema"

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def find_all(cls):
        query = "SELECT * from dojos"
        return connectToMySQL(DATABASE).query_db(query)
