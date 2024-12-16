from flask import Flask
from flask_pymongo import PyMongo

# Initialize the PyMongo extension
mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Set up the MongoDB URI (make sure to replace with your actual URI)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/ecommerce_db"

    # Initialize the app with PyMongo
    mongo.init_app(app)

    # Import routes after app initialization to avoid circular imports
    from app import routes
    app.register_blueprint(routes.bp)

    return app
