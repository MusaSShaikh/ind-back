from flask import Blueprint, jsonify
from app import mysql

data_api = Blueprint('data_api', __name__)

@data_api.route('/api/data')
def get_data():
    try:
        cursor = mysql.connection.cursor()
        query = """
        SELECT film.film_id, title, category.category_id, name
        FROM film
        INNER JOIN film_category ON film.film_id = film_category.film_id
        INNER JOIN category ON film_category.category_id = category.category_id
        """
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        if data:
            return jsonify(data)
        else:
            return jsonify({'error': 'No data found in the database'})
    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching data: {}'.format(str(e))})

# Register blueprint
from app import app
app.register_blueprint(data_api)
