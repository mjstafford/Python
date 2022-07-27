from app.config.mysqlconnection import connectToMySQL
from app import DATABASE

class Category:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def find_all(cls):
        query = "SELECT * FROM categories"
        results = connectToMySQL(DATABASE).query_db(query)

        all_categories = []

        for row in results:
            curr_category = Category(row)
            all_categories.append(curr_category)
        
        return all_categories

    @classmethod
    def save(cls, data):
        query = "INSERT INTO categories_has_blogs (categories_id, blogs_id) VALUES (%(categories_id)s, %(blogs_id)s)"
        return connectToMySQL(DATABASE).query_db(query, data)