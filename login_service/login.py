from flask import Flask, request, jsonify
import requests
import os


app = Flask(__name__)

DATABASE_SERVICE_URL=os.getenv("DATABASE_SERVICE_URL")

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    try:
        response = requests.get(f"{DATABASE_SERVICE_URL}/users/{username}")
        if response.status_code == 200:
            user = response.json()
            print(response.content)
            if user["password"] == password:
                return jsonify({"message": "Login successful", "user_id": user['id']}), 200
            else:
                return jsonify({"error": "Invalid password"}), 401
        else:
            return jsonify({"error": "User not found"}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to communicate with database service: {str(e)}"}), 500



@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400
    
    try:
        response = requests.post(f"{DATABASE_SERVICE_URL}/register", json=data)
        if response.status_code == 201:
            return jsonify({"message": "User registered"}), 201
        else:
            return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Couldn't reach database or user already exists, error: {str(e)}"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)