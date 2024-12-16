from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017")
db = client["ecommerce_db"]  # Use your database
collection = db["products"]  # Use your products collection

@app.route('/api/products', methods=['GET'])
def get_products():
    # Fetch data from MongoDB
    products = list(collection.find({}, {'_id': 0}))  # Remove MongoDB's default _id field
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
