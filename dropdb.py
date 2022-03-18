
import mysql.connector
from data.config import HOST, USER, PASSWORD, DBNAME

conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DBNAME
)

cursor = conn.cursor()
cursor.execute(f"DROP DATABASE {DBNAME};")
cursor.close()
conn.close()
