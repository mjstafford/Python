from flask import flash, session
from app import DATABASE, EMAIL_REGEX, app
from app.config.mysqlconnection import connectToMySQL

class Blog:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.user_id = data["user_id"]

    @classmethod
    def find_by_category(cls, data):
        query = "SELECT * from blogs LEFT JOIN categories_has_blogs ON blogs.id = blogs_id LEFT JOIN categories ON categories.id = categories_id WHERE name = %(name)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        print(results)
        all_blogs = []
        for row in results:
            curr_blog = Blog(row)
            curr_blog.category = row["name"]
            all_blogs.append(curr_blog)

        return all_blogs

    @classmethod
    def sort_by_date(cls):
        query = "SELECT * from blogs ORDER BY created_at LIMIT 5;"
        results = connectToMySQL(DATABASE).query_db(query)

        recent_blogs = []
        for row in results:
            curr_blog = Blog(row)
            recent_blogs.append(curr_blog)

        return recent_blogs

    @staticmethod
    def validate_blog(data):
        is_valid = True

        if data["title"] == "":
            flash("title cannot be blank", "title_error")
            is_valid = False
        elif len(data["title"]) < 3:
            flash("title needs to have at least 3 chars", "title_error")
            is_valid = False

        if data["description"] == "":
            flash("description cannot be blank", "description_error")
            is_valid = False
        elif len(data["description"]) < 20:
            flash("description needs to have at least 20 chars", "description_error")
            is_valid = False

        return is_valid