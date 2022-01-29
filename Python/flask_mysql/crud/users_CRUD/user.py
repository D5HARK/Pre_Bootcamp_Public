from mysqlconnection import connecttoMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connecttoMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s);"
        result = connecttoMySQL("users_schema").query_db(query, data)
        return result

    @classmethod
    def get_user(cls, user_id):
        query = f'SELECT * FROM users WHERE id = {user_id};'
        result = connecttoMySQL('users_schema').query_db(query)
        profile = []
        for user in result:
            profile.append(cls(user))
        return profile

    @classmethod
    def edit_user(cls, new_data):
        query = 'UPDATE users SET first_name = %(new_f_name)s, last_name = %(new_l_name)s WHERE id = %(id)s;'
        result = connecttoMySQL("users_schema").query_db(query, new_data)
        return result


    @classmethod
    def delete(cls, user_id):
        query = 'DELETE FROM users WHERE id = %(id)s'
        result = connecttoMySQL("users_schema").query_db(query, user_id)
        return result
