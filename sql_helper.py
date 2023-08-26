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
        conn.commit()
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
        c.execute(f"""INSERT INTO circle(name, owner_id) VALUES('{circlename}', {owner_id});""")
        c.execute(f"""INSERT INTO belongsTo(user_id, circle_id, admin) VALUES({owner_id}, (SELECT (MAX(id) + 1) from circle), TRUE);""")
        conn.commit()
    except Exception as e:
        print(e)

def user_join_circle(conn: sqlite3.Connection, user_id: int, circle_id: int):
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO belongsTo(user_id, circle_id, admin) VALUES({user_id}, {circle_id}, FALSE);""")
        conn.commit()
    except Exception as e:
        print(e)

def add_task(conn: sqlite3.Connection, user_id: int, circle_id: int, name: str, description: str):
    try:
        c = conn.cursor()
        c.execute(f"""INSERT INTO task(user_id, circle_id, completed, name, description) VALUES({user_id}, {circle_id}, FALSE, '{name}', '{description}');""")
        conn.commit()
    except Exception as e:
        print(e)

def get_user_tasks(conn: sqlite3.Connection, user_id: int, circle_id: int = -1):
    try:
        # c = conn.cursor()
        if circle_id == -1:
            return pd.read_sql(f"SELECT * FROM task WHERE user_id = {user_id} GROUP BY circle_id;", con=conn)
            # c.execute(f"""SELECT * FROM task WHERE user_id = {user_id} GROUP BY circle_id;""")
        else:
            return pd.read_sql(f"SELECT * FROM task WHERE user_id = {user_id} AND circle_id = {circle_id};", con=conn)
            # c.execute(f"""SELECT * FROM task WHERE user_id = {user_id} AND circle_id = {circle_id};""")
        # records = c.fetchall()
        # return records
    except Exception as e:
        print(e)

def get_group_users(conn: sqlite3.Connection, circle_id: int):
    try:
        # c = conn.cursor()
        # c.execute(f"""SELECT * FROM user WHERE id IN (SELECT user_id FROM belongsTo WHERE circle_id = {circle_id});""")
        # records = c.fetchall()
        return pd.read_sql(sql=f"SELECT * FROM user WHERE id IN (SELECT user_id FROM belongsTo WHERE circle_id = {circle_id});", con=conn)
    except Exception as e:
        print(e)

def get_user_groups(conn: sqlite3.Connection, user_id:int):
    #cmd = f"""
    #        SELECT name FROM circle 
    #        WHERE EXISTS (
    #            SELECT circle_id FROM user JOIN belongsTo ON (user.id = belongsTo.user_id)
    #            WHERE user.id = {user_id}
    #        );
    #    """
    cmd = f"SELECT id FROM circle WHERE id IN (SELECT circle_id FROM belongsTo WHERE user_id = {user_id});"
    try:
        return pd.read_sql(sql=cmd,con=conn)['id']
    except Exception as e:
        print(e)

def complete_task(conn: sqlite3.Connection, username: int):
    try:
        return pd.read_sql(sql=f"SELECT id FROM user WHERE name = '{username}'", con=conn)
    except Exception as e:
        print(e)


def get_user_id_by_username(conn: sqlite3.Connection, username: str) -> int:
    try:
        return int(pd.read_sql(sql=f"SELECT id FROM user WHERE name = '{username}'", con=conn)["id"])
    except Exception as e:
        print(e)


def get_circlename_by_circle_id(conn: sqlite3.Connection, circle_id: int) -> str:
    try:
        return pd.read_sql(sql=f"SELECT name FROM circle WHERE id = {circle_id}", con=conn).values.tolist()[0][0]
    except Exception as e:
        print(e)

