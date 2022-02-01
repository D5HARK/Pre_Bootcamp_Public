from flask_app.config.mysqlconnection import connecttoMySQL

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.time = data["30_min"]
        self.date = data["date_made"]
        self.created = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connecttoMySQL('recipes_schema').query_db(query)
        recipes = []
        for  recipe in results:
            recipes.append (cls(recipe))
        return recipes
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, date_made, 30_min) VALUES (%(name)s, %(description)s, %(instructions)s, %(date_made)s, %(30_min)s)"
        result = connecttoMySQL("recipes_schema").query_db(query, data)
        return result

    @classmethod
    def get_recipe(cls, recipe_id):
        query = f'SELECT * FROM recipes WHERE id = {recipe_id};'
        result = connecttoMySQL("recipes_schema").query_db(query)
        recipe = []
        for item in result:
            recipe.append(cls(item))
        return recipe

    @classmethod
    def edit_recipe(cls, new_data):
        query = 'UPDATE urecipes SET name = %(new_name)s, description = %(new_description)s, instructions = %(new_instructions)s, date_made = %(new_date)s, 30_min = %(new_30)s WHERE id = %(id)s;'
        result = connecttoMySQL("recipes_schema").query_db(query, new_data)
        return result

    @classmethod
    def delete(cls, recipe_id):
        query = 'DELETE FROM recipes WHERE id = %(id)s'
        result = connecttoMySQL("recipes_schema").query_db(query, recipe_id)
        return result

