from flask import Flask, render_template, Blueprint
from data.config import HOST, USER, DBNAME, PASSWORD
from app.start_view import start
from app.main_view import main
from app.db import mysql

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DBNAME
app.config['MYSQL_DATABASE_HOST'] = HOST
mysql.init_app(app)


app.register_blueprint(start)
app.register_blueprint(main)


@app.route('/building')
def building():
    print("bulding")
    return 'Your route is building...'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


if __name__ == '__main__':
    app.run(debug=True)
