from flask import Flask, jsonify, request

app = Flask(__name__)

# Singleton to manage users
class UserManager:
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
    ]

    @classmethod
    def get_users(cls):
        return cls.users

    @classmethod
    def reset_users(cls):
        cls.users = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
        ]

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(UserManager.get_users()), 200

# Get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in UserManager.get_users() if user["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    if not new_user.get("name") or not new_user.get("email"):
        return jsonify({"error": "Name and email are required"}), 400
    new_user["id"] = len(UserManager.get_users()) + 1
    UserManager.get_users().append(new_user)
    return jsonify(new_user), 201

# Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in UserManager.get_users() if user["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    updated_data = request.json
    user.update(updated_data)
    return jsonify(user), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in UserManager.get_users() if user["id"] != user_id]
    UserManager.users = users
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
