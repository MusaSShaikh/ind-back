from flask import Flask, Blueprint, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_api = Blueprint('data_api', __name__)

# Sample data
data = ["Item 1", "Item 2", "Item 3"]

@data_api.route('/api/data')
def get_data():
    return jsonify(data)

# Register blueprint
app.register_blueprint(data_api)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
