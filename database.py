import sqlite3
from datetime import datetime

DB_PATH = 'posts.db'

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER NOT NULL,
        title TEXT NOT NULL,
        img TEXT NOT NULL,
        content TEXT NOT NULL,
        author TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_post(post: dict):
    conn = get_conn()
    c = conn.cursor()
    c.execute("""
    INSERT INTO posts (id, title, img, content, author, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (post['id'], post['title'], post['img'], post['content'], post['author'], post['created_at']))

    conn.commit()
    conn.close()
    return True

def delete_post(post_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    conn.commit()
    changes = c.rowcount
    conn.close()
    return changes > 0

def get_all_posts():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY created_at DESC")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]
