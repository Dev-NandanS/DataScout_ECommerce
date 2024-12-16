from flask import Blueprint, jsonify
from . import mongo  # Importing mongo to interact with the MongoDB database

bp = Blueprint('routes', __name__)

@bp.route('/api/products', methods=['GET'])
def get_products():
    # Fetch data from MongoDB
    products = list(mongo.db.products.find({}, {'_id': 0}))  # Remove MongoDB's default _id field
    return jsonify(products)
