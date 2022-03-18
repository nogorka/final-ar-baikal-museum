import mysql.connector
from data.config import HOST, USER, PASSWORD, DBNAME


def read_file(file_path):
    with open(file_path, mode='r', encoding="utf-8") as f:
        return f.read()


def open_connection(name):
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=name,
        charset='utf8',
        use_unicode=True
    )


files = ['data/create_tables.sql',
         'data/fill_database.sql',
         'data/fill_stat.sql'
         ]

sql = []
for file in files:
    text = (read_file(file)).replace('\n',"")
    for line in text.split(';'):
        if line:
            sql.append(line)


conn = open_connection(None)
with conn.cursor() as cursor:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DBNAME};")
    conn.commit()
    cursor.close()
conn.close()

conn = open_connection(DBNAME)
with conn.cursor() as cursor:
    for query in sql:
        cursor.execute(query, multi=True)
        conn.commit()
    cursor.close()
conn.close()
