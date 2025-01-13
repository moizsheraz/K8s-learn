from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://mongodb:27017/")
db = client.userdb
users_collection = db.users

@app.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user["_id"] = str(user["_id"])  # Convert ObjectId to string
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
