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
        # self.dojo_id = data["updated_at"]
        #probably need id for dojo here
        
    @classmethod
    def find_all(cls):
        query = "SELECT * from dojos"
        return connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def save(cls, data):
        # add in the foreign key as a value (not required in instance attribute though?)
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)