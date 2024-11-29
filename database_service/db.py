from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE_FILE = "database.db"

def init_db():
    if not os.path.exists(DATABASE_FILE):
        connection = sqlite3.connect(DATABASE_FILE)
        with open("init.sql", "r") as f:
            connection.executescript(f.read())
        connection.close()

def query_db(query, args=(), one=False):
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.execute(query, args)
    rv = cursor.fetchall()
    connection.commit()
    connection.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/register', methods=['POST'])
def create_user():
    data = request.json
    try:
        query_db("INSERT INTO users (username, password) VALUES (?, ?)",
                (data['username'], data['password']))
        return jsonify({"message": "User created!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "User already exists!"}), 400

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    query_db("INSERT INTO tasks (user_id, description) VALUES (?, ?)",
             (data['user_id'], data['description']))
    return jsonify({"message": "Task created!"}), 201
    
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    query_db("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    return jsonify({"message": "Task completed!"}), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    query_db("DELETE FROM tasks where id = ?", (task_id,))
    return jsonify({"message": "Task deleted!"}), 200

@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    tasks = query_db("SELECT * FROM tasks where user_id = ?", (user_id,))
    if not tasks:
        return jsonify({"message": "no such tasks found for this user"}), 404
    return jsonify([dict(task) for task in tasks]), 200

@app.route('/users/<username>', methods=['GET'])
def get_user_by_username(username):
    user = query_db("SELECT * FROM users WHERE username = ?", (username,), one=True)
    if user:
        return jsonify(dict(user)), 200
    else:
        return jsonify({"error": "User not found"}), 404



if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5002, debug=True)