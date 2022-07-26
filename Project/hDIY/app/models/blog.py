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
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        query = "SELECT * from blogs ORDER BY created_at LIMIT 5;"
        results = connectToMySQL(DATABASE).query_db(query)
        print("HELLO RESULTS")
        print(results)

        recent_blogs = []
        for row in results:
            curr_blog = Blog(row)
            recent_blogs.append(curr_blog)

        print(recent_blogs)
        return recent_blogs