import os
import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'board.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize DB on start
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/posts', methods=['GET'])
def get_posts():
    try:
        conn = get_db_connection()
        # Fetching posts in descending order (newest first)
        posts = conn.execute(
            "SELECT id, title, message, strftime('%Y-%m-%d %H:%M:%S', created_at) as created_at FROM posts ORDER BY id DESC"
        ).fetchall()
        conn.close()
        return jsonify([dict(post) for post in posts]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/posts', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        title = data.get('title', '').strip()
        message = data.get('message', '').strip()
        
        if not title or not message:
            return jsonify({"error": "Title and message are required"}), 400
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO posts (title, message) VALUES (?, ?)",
            (title, message)
        )
        conn.commit()
        
        # Get the newly inserted post
        new_id = cursor.lastrowid
        new_post = conn.execute(
            "SELECT id, title, message, strftime('%Y-%m-%d %H:%M:%S', created_at) as created_at FROM posts WHERE id = ?",
            (new_id,)
        ).fetchone()
        conn.close()
        
        return jsonify(dict(new_post)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    try:
        conn = get_db_connection()
        # Verify post existence
        post = conn.execute("SELECT id FROM posts WHERE id = ?", (post_id,)).fetchone()
        if not post:
            conn.close()
            return jsonify({"error": "Post not found"}), 404
        
        conn.execute("DELETE FROM posts WHERE id = ?", (post_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": f"Post {post_id} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Running flask on port 5000 in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
