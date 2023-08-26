import sqlite3
import pandas as pd

def get_conn_object(file_path):
    conn = None
    try:
        conn = sqlite3.connect(file_path)
        return conn
    except Exception as e:
        print(e)
    return conn


def execute_commands(conn: sqlite3.Connection, cmd: str):
    try:
        c = conn.cursor()
        c.executescript(cmd)
    except Exception as e:
        print(e)

def retrieve_table(conn: sqlite3.Connection, cmd: str):
    try:
        return pd.read_sql(sql = cmd, con = conn)
    except Exception as e:
        print(e)


def add_user(conn: sqlite3.Connection, username: str):
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO user("name") VALUES('{username}');""")
        conn.commit()
    except Exception as e:
        print(e)

def add_circle(conn: sqlite3.Connection, circlename: str, owner_id: int):
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO cirle(name, owner_id) VALUES('{circlename}', {owner_id});""")
        c.execute(f"""INSERT INTO belongsTo(user_id, circle_id, admin) VALUES({owner_id}, (SELECT MAX(id) from circle), TRUE""")
        conn.commit()
    except Exception as e:
        print(e)

def user_join_circle(conn: sqlite3.Connection, user_id: int, circle_id: int):
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO belongsTo(user_id, circle_id, admin) VALUES({user_id}, {circle_id}, FALSE""")
        conn.commit()
    except Exception as e:
        print(e)

def add_task(conn: sqlite3.Connection, user_id: int, circle_id: int, name: str, description: str):
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO belongsTo(user_id, circle_id, completed, name, description) VALUES({user_id}, {circle_id}, FALSE, '{name}', '{description}'""")
        conn.commit()
    except Exception as e:
        print(e)

# conn = get_conn_object("./data.db")
# # add_user(conn, "Ivan")

# cmd = """
# DROP TABLE IF EXISTS user;
# DROP TABLE IF EXISTS circle;
# DROP TABLE IF EXISTS task;
# DROP TABLE IF EXISTS belongsTo;

# CREATE TABLE user (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT
# );

# CREATE TABLE circle (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     owner_id INTEGER,
#     name TEXT,
#     FOREIGN KEY (owner_id) REFERENCES user (id)
# );

# CREATE TABLE belongsTo (
#     user_id INTEGER NOT NULL,
#     circle_id INTEGER NOT NULL,
#     admin INTEGER,
#     FOREIGN KEY (user_id) REFERENCES user (id),
#     FOREIGN KEY (circle_id) REFERENCES circle (id),
#     PRIMARY KEY (user_id, circle_id)
# );

# CREATE TABLE task (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     user_id INTEGER NOT NULL,
#     circle_id INTEGER NOT NULL,
#     completed INTEGER,
#     name TEXT,
#     description TEXT
# );
# """

# execute_commands(conn, cmd)

# conn.close()