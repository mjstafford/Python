from app.config.mysqlconnection import connectToMySQL

DATABASE = "dojos_and_ninjas_schema"

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        #probably need id for dojo here
        
    @classmethod
    def find_all(cls):
        query = "SELECT * from dojos"
        return connectToMySQL(DATABASE).query_db(query)