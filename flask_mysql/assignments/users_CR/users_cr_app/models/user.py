# name of model is singular!
from users_cr_app.config.mysqlconnection import connectToMySQL  # this is a helper function in the mysqlconnection file that allows you to create an instance of the class

class User:
    def __init__(self, data):   #will take in data from controller a create a class instance of a db record
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        #create a query
        #query db which returns a list of dicts (but they are not instances yet!)
        #iterate over that list and turn each dict into a Class Instance and then add that to a list
        #now you have a list of class instances (which have access to all their methods etc.)
        #return the list, so that the controller can send that info to the template!
        query = "SELECT * FROM users;"
        #connectToMySQL('users_schema') connects to the db via this instance
        #using a .query_db(query) method!
        raw_users_from_db = connectToMySQL('users_schema').query_db(query)
        users_instances = []
        for user_in_dict in raw_users_from_db:
            users_instances.append(User(user_in_dict))
        return users_instances

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        print("trying to save ...in model")
        return connectToMySQL('users_schema').query_db(query, data) # dont forget to add the data!
    
