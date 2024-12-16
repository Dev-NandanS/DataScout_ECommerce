import csv
from pymongo import MongoClient
import re  # Regular expressions to handle non-numeric values

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017")  # Your MongoDB URI
db = client["ecommerce_db"]  # Your database name
collection = db["products"]  # Your collection name

# Function to clean up values (remove currency symbols and commas)
def clean_price(price):
    return price.replace("â‚¹", "").replace(",", "").strip()

# Function to safely convert rating to float
def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return None  # If conversion fails, return None

# Function to safely convert a value to an integer
def safe_int(value):
    # Remove any non-numeric characters before trying to convert to integer
    numeric_value = re.sub(r'[^\d]', '', value)
    if numeric_value:
        return int(numeric_value)
    return 0  # Default to 0 if no valid integer value is found

# Open CSV and insert into MongoDB
with open('C:/Users/anand/Downloads/archive (1)/Amazon-Products.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Read CSV into a dictionary
    products = []

    for row in reader:
        product = {
            "name": row["name"].strip(),
            "main_category": row["main_category"].strip(),
            "sub_category": row["sub_category"].strip(),
            "image": row["image"].strip(),
            "link": row["link"].strip(),
            "ratings": safe_float(row["ratings"].strip()) if row["ratings"] else None,
            "no_of_ratings": safe_int(row["no_of_ratings"].strip()),  # Use safe_int here
            "discount_price": clean_price(row["discount_price"]),
            "actual_price": clean_price(row["actual_price"])
        }
        products.append(product)

    # Insert into MongoDB
    collection.insert_many(products)

print("Data inserted into MongoDB!")
