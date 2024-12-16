from flask import Flask
from flask_pymongo import PyMongo
import os

def create_app():
    app = Flask(__name__)
    
    # Configure the MongoDB URI
    app.config["MONGO_URI"] = "mongodb://localhost:27017/ecommerce_db"  # Your MongoDB URI
    mongo = PyMongo(app)  # Initialize MongoDB
    
    from . import routes
    app.register_blueprint(routes.bp)  # Register routes

    return app
