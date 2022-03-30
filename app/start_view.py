from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .logic.route_building import build_route
from .db import mysql

start = Blueprint('start', __name__)


@start.route('/guide')
def index():
    return render_template('guide_start/start_page.html')


@start.route('/generated')
def generated():
    return render_template('guide_start/generated.html')


@start.route('/predefined')
def predefined():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * from predefinedroutes;')
    data = cursor.fetchall()
    return render_template('guide_start/predefined.html', routes=data)


@start.route('/custom')
def custom():
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("""SELECT e.id, e.name, r.name 
                    from entities as e, rooms as r 
                    where e.roomId = r.id;""")
    data = cursor.fetchall()
    dict_data = {}

    for it in data:
        if it[2] in dict_data.keys():
            value = dict_data.get(it[2])
            value.append([it[0], it[1]])
        else:
            dict_data[it[2]] = [[it[0], it[1]]]

    return render_template('guide_start/custom.html', rooms=dict_data)


@start.route('/build_route', methods=['POST'])
def build_current_route():
    route = build_route(request.json)

    return jsonify(route=route)
