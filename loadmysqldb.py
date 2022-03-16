
import mysql.connector
import os
from data.config import HOST, USER, PASSWORD, DBNAME

_DBNAME = DBNAME
dir_path = 'data'
SQL = f"CREATE DATABASE IF NOT EXISTS {_DBNAME}; SHOW DATABASES; USE {_DBNAME}; "

# TODO: truncate tables


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


os.chdir(dir_path)
for file in os.listdir():
    if file.endswith('.sql'):
        SQL += read_file(f"{file}")


conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD
)

cursor = conn.cursor(buffered=True)
cursor.execute(SQL, multi=True)

conn.commit()
conn.close()


# cursor.execute(f"DROP DATABASE {_DBNAME};")
