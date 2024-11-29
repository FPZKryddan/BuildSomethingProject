from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DATABASE_SERVICE_URL = os.getenv("DATABASE_SERVICE_URL")

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    try:
        response = requests.post(f"{DATABASE_SERVICE_URL}/tasks", json=data)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to communicate with database service: {str(e)}"}), 500


@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    try:
        response = requests.get(f"{DATABASE_SERVICE_URL}/tasks/{user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to communicate with database service: {str(e)}"}), 500


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    try:
        response = requests.put(f"{DATABASE_SERVICE_URL}/tasks/{task_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to communicate with database service: {str(e)}"}), 500


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        response = requests.delete(f"{DATABASE_SERVICE_URL}/tasks/{task_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to communicate with database service: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
