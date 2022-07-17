from app.config.mysqlconnection import connectToMySQL
from app import DATABASE
#special non-circular import
from app.models import book

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.fav_books = []

    @classmethod
    def find_all(cls):
        query = "SELECT * FROM users;"
        users_raw = connectToMySQL(DATABASE).query_db(query)
        users_list = []
        for user in users_raw:
            users_list.append( cls (user))
        return users_list

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s,%(last_name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)


    @classmethod
    def get_user_by_id(cls,data):
        query= "SELECT * FROM users where users.id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_all_fav_books(cls, data):
        query  = "SELECT * FROM users " 
        query += "LEFT JOIN favorites ON users.id = favorites.user_id " 
        query += "LEFT JOIN books ON books.id = favorites.book_id " 
        query += "WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)

        if results[0]["books.id"] == None :
            return False

        curr_user = cls (results[0])         #turn 1 into author

        for fav_book in results:         #turn into books & append
            print(fav_book)
            fav_book_data = {
                "id" : fav_book["books.id"],
                "title" : fav_book["title"],
                "num_of_pages" : fav_book["num_of_pages"],
                "created_at" : fav_book["books.created_at"],
                "updated_at" : fav_book["books.updated_at"]
            }

            curr_user.fav_books.append(book.Book(fav_book_data))

        return curr_user.fav_books