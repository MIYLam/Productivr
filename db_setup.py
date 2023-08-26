import sqlite3

def execute_commands(conn: sqlite3.Connection, cmd: str):
    try:
        c = conn.cursor()
        c.executescript(cmd)
        conn.commit()
    except Exception as e:
        print(e)

def get_conn_object(file_path):
    conn = None
    try:
        conn = sqlite3.connect(file_path)
        return conn
    except Exception as e:
        print(e)
    return conn

conn = get_conn_object("./data.db")

cmd = """
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS circle;
DROP TABLE IF EXISTS task;
DROP TABLE IF EXISTS belongsTo;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE circle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER,
    name TEXT,
    FOREIGN KEY (owner_id) REFERENCES user (id)
);

CREATE TABLE belongsTo (
    user_id INTEGER NOT NULL,
    circle_id INTEGER NOT NULL,
    admin INTEGER,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (circle_id) REFERENCES circle (id),
    PRIMARY KEY (user_id, circle_id)
);

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    circle_id INTEGER NOT NULL,
    completed INTEGER,
    name TEXT,
    description TEXT
);
"""

execute_commands(conn, cmd)

conn.close()