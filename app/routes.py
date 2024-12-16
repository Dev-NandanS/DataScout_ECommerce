from flask import Blueprint, render_template, request
from app import mongo

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search_query')  # Get the search query from the URL
    products = []
    
    if search_query:
        # Perform the search in the database (matching against 'name' or 'description')
        products = mongo.db.products.find({
            '$or': [
                {'name': {'$regex': search_query, '$options': 'i'}},  # Case-insensitive match on name
                {'description': {'$regex': search_query, '$options': 'i'}}  # Case-insensitive match on description
            ]
        })
    else:
        # If there's no search query, return all products
        products = mongo.db.products.find()
    
    return render_template('index.html', products=products)

