from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from data.config import HOST, USER, DBNAME, PASSWORD
from backend.route_building import build_route

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DBNAME
app.config['MYSQL_DATABASE_HOST'] = HOST
mysql.init_app(app)


@app.route('/')
def index():
    return render_template('start_page.html')


@app.route('/predefined', methods=['GET', 'POST'])
def predefined():
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from predefinedroutes;")
        data = cursor.fetchall()
        return render_template('predefined.html', routes=data)
    elif request.method == 'POST':
        print('received json', request.json)
        # TODO - invoke building method or checking build method
        return redirect(url_for('building'))


@app.route('/generated', methods=['GET', 'POST'])
def generated():
    if request.method == 'GET':
        return render_template('generated.html')
    else:
        # TODO - invoke building method or checking build method
        return redirect(url_for('building'))


@app.route('/custom', methods=['GET', 'POST'])
def custom():
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT e.id, e.name, r.name from entities as e, rooms as r where e.roomId = r.id;")
        data = cursor.fetchall()
        dict_data = {}

        for it in data:
            if it[2] in dict_data.keys():
                value = dict_data.get(it[2])
                value.append([it[0], it[1]])
            else:
                dict_data[it[2]] = [[it[0], it[1]]]

        return render_template('custom.html', rooms=dict_data)
    elif request.method == 'POST':

        # TODO - invoke building method or checking build method
        return redirect(url_for('building'))


@app.route('/building')
def building():
    print("bulding")
    return 'Your route is building...'


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


if __name__ == '__main__':
    app.run(debug=True)
