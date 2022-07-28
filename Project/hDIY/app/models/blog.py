from flask import flash, session
from app import DATABASE, EMAIL_REGEX, app
from app.config.mysqlconnection import connectToMySQL
from app.models import category

class Blog:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO blogs (title, description, user_id) VALUES (%(title)s,%(description)s,%(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def find_by_category(cls, data):
        query = "SELECT * FROM blogs LEFT JOIN categories_has_blogs ON blogs.id = categories_has_blogs.blogs_id LEFT JOIN categories ON categories.id = categories_id LEFT JOIN favorites ON blogs.id = favorites.blogs_id WHERE name = %(name)s"
        # query = "SELECT * from blogs LEFT JOIN categories_has_blogs ON blogs.id = blogs_id LEFT JOIN categories ON categories.id = categories_id WHERE name = %(name)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        print("\nHERE\n",results)
        all_blogs = []
        for row in results:
            curr_blog = Blog(row)
            curr_blog.category = row["name"]
            all_blogs.append(curr_blog)
            if "users_id" in row and row["users_id"] == session["user_id"]:
                curr_blog.is_user_favorite = True

        return all_blogs

    @classmethod
    def find_by_id_with_categories(cls, data):
        query = "SELECT * FROM blogs LEFT JOIN categories_has_blogs ON blogs.id = blogs_id LEFT JOIN categories ON categories.id = categories_id WHERE blogs.id = %(id)s"
        blog_data = connectToMySQL(DATABASE).query_db(query,data)   #returns a list of the same blog with rows of different categories details
        if len(blog_data) == 0:
            return None

        blog = Blog(blog_data[0])
        blog_categories = [] 

        for row in blog_data:
            data = {
                **row,
                "id" : row["categories.id"],
                "created_at" : row["categories.created_at"],
                "updated_at" : row["categories.updated_at"]
            }
            blog_categories.append(category.Category(data))
        blog.categories = blog_categories

        return blog

    @classmethod
    def toggle_favorite(cls,data):
        query = "SELECT * from favorites WHERE blogs_id = %(blogs_id)s AND users_id= %(users_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)

        #if user has not favorited this blog
        if( len(result) == 0):
            return cls.add_favorite(data)

        #if user has favorited this blog, unfavorite it!
        return cls.remove_favorite(data)

    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (blogs_id,users_id) VALUES (%(blogs_id)s, %(users_id)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def remove_favorite(cls,data):
        query = "DELETE FROM favorites WHERE blogs_id = %(blogs_id)s AND users_id= %(users_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def find_all_favorites_of_user(cls, data):
        query = "SELECT * FROM favorites LEFT JOIN blogs ON blogs_id = blogs.id WHERE users_id = %(user_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)    #returns false? if there are no results?

        if not results:
            return None

        print(results)

        all_favorite_blogs = []
        for row in results:
            curr_blog = Blog(row)
            all_favorite_blogs.append(curr_blog)

        return all_favorite_blogs

    @classmethod
    def is_favorite(cls, data):
        query = "SELECT * FROM favorites LEFT JOIN blogs ON blogs_id = blogs.id WHERE users_id = %(user_id)s AND blogs_id = %(blog_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)  
        return len(results) > 0

    @classmethod
    def sort_by_date(cls):
        query = "SELECT * from blogs ORDER BY created_at DESC LIMIT 4;"
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