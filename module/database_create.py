from database import connection

def create_table():
    condition=False
    path_table = '''CREATE TABLE path (
        path_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL,
        description TEXT
    )'''
    connection(path_table,condition)
    venv_table = '''CREATE TABLE venv (
        venv_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        path TEXT NOT NULL,
        description TEXT
    )'''
    connection(venv_table,condition)
    print('Database Table Created Successfully')

create_table()