from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# MongoDB Atlas connection
load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client['todo_database']
collection = db['todo_items']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    
    # Store data in MongoDB
    todo_item = {"name": item_name, "description": item_description}
    collection.insert_one(todo_item)
    
    return "To-Do Item Submitted Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
