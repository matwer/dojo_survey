from flask import flash

from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.crated_at = data['created_at']
        self.updated_at = data['updated_at']


    # READ

    # gets one user and returns the user with a matching user id
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL("dojo_survey_schema").query_db(query,data)

        this_user = cls(results[0])

        return this_user


    # creates a new user and inserts the user into the daatabase
    @classmethod
    def add_user(cls,data):
        query = "INSERT INTO users (name, location, language, comment, created_at, updated_at) " \
            "VALUES (%(user_name)s, %(location)s, %(language)s, %(comments)s, NOW(), NOW());"
        
        user_id = connectToMySQL("dojo_survey_schema").query_db(query,data)

        return user_id

    # this is a static method becuase we just need to validate the data but we don't need 
    # references to the instance or the class
    @staticmethod
    def validate_user(post_data): # post-data is the data we'll recieve from the form
        is_valid = True # we assume the data is valid so we set it to true at the start

        print(post_data['user_name'])
        print(post_data['location'])
        print(post_data['language'])
        print(post_data['comments'])


        # flash is a message that exists for a single request-response cycle
        # for each validation, nottify the user and change the boolean to false
        if len(post_data['user_name']) < 3:
            flash("Name must be at least 3 characters.") 
            is_valid = False 
    
        if len(post_data['location']) < 3:
            flash("Location is required. Select a location from the drop down.")
            is_valid = False
    
        if len(post_data['language']) < 3:
            flash("Language is required. Select a favorite language from the drop down.")
            is_valid = False
    
        if len(post_data['comments']) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
    
        return is_valid
