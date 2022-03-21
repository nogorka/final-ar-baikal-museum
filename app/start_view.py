from flask import Blueprint, render_template, request, redirect, url_for
from .route_logic.route_building import build_route
from .db import mysql

start = Blueprint('start', __name__)


@start.route('/guide')
def index():
    return render_template('start_page.html')


@start.route('/generated', methods=['GET', 'POST'])
def generated():
    if request.method == 'GET':
        return render_template('generated.html')
    else:
        build_route(request.json)
        return redirect(url_for('building'))


@start.route('/predefined', methods=['GET', 'POST'])
def predefined():
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from predefinedroutes;")
        data = cursor.fetchall()
        return render_template('predefined.html', routes=data)
    elif request.method == 'POST':
        # print('received json', request.json)
        build_route(request.json)
        return redirect(url_for('building'))


@start.route('/custom', methods=['GET', 'POST'])
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
        # print('received json', request.json)

        build_route(request.json)
        return redirect(url_for('building'))

