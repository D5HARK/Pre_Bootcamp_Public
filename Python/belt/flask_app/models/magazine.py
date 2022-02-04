from flask_app.config.mysqlconnection import connecttoMySQL

class Magazine:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM magazines;"
        results = connecttoMySQL('magazines').query_db(query)
        magazines = []
        for  item in results:
            magazines.append (cls(item))
        return magazines
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO magazines (title, description) VALUES (%(title)s, %(description)s)"
        result = connecttoMySQL("magazines").query_db(query, data)
        return result

    @classmethod
    def get_magazine(cls, magazine_id):
        query = f'SELECT * FROM magazines WHERE id = {magazine_id};'
        result = connecttoMySQL("magazines").query_db(query)
        magazine = []
        for item in result:
            magazine.append(cls(item))
        return magazine

    @classmethod
    def edit_magazine(cls, new_data):
        query = 'UPDATE magazines SET title = %(new_title)s, description = %(new_description)s WHERE id = %(id)s;'
        result = connecttoMySQL("magazines").query_db(query, new_data)
        return result

    @classmethod
    def delete(cls, magazine_id):
        query = 'DELETE FROM magazines WHERE id = %(id)s'
        result = connecttoMySQL("magazines").query_db(query, magazine_id)
        return result

