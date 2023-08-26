import sqlite3

def get_conn_object(file_path):
    conn = None
    try:
        conn = sqlite3.connect(file_path)
        return conn
    except Exception as e:
        print(e)
    return conn

def execute_commands(conn, cmd):
    try:
        c = conn.cursor()
        c.execute(cmd)
    except Exception as e:
        print(e)