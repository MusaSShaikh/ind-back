from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pass1234'
app.config['MYSQL_DB'] = 'sakila'

mysql = MySQL(app)

# Import routes after initializing Flask app
import routes

if __name__ == '__main__':
    app.run(debug=True, port=5000)
