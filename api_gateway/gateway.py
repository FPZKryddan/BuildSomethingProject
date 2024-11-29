from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

LOGIN_SERVICE_URL = os.getenv("LOGIN_SERVICE_URL")
TASK_SERVICE_URL = os.getenv("TASK_SERVICE_URL")


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        response = requests.post(f"{LOGIN_SERVICE_URL}/login", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        response = requests.post(f"{LOGIN_SERVICE_URL}/register", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
        

@app.route('/tasks/<int:user_id>', methods=['GET'])
def list_tasks(user_id):
    try:
        response = requests.get(f"{TASK_SERVICE_URL}/tasks/{user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)