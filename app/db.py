from flaskext.mysql import MySQL

mysql = MySQL()


def mysql_select(sql):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(sql)
    return cursor.fetchall()