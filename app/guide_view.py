from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .logic.route_building import build_route, get_directions, parse_route_direct
from .db import mysql

guide = Blueprint('guide', __name__)


@guide.route('/route')
def route():

    depart = request.args.get('depart')
    dest = request.args.get('dest')

    route = get_directions(depart, dest)
    msg_route = parse_route_direct(route).capitalize()
    name = f"Путь от {depart} до {dest}"

    data = get_data(dest)
    _, targetUri, overlayType, overlayUri = data[0]

    return render_template('guide_nav/route_message.html', name=name, message=msg_route, marker_src=targetUri)


@guide.route('/show/<entity_id>')
def show(entity_id):

    data = get_data(entity_id)

    name, targetUri, overlayType, overlayUri = data[0]

    template = 'guide_nav/'

    if overlayType == 3:
        template += 'overlay_model.html'
    if overlayType == 2:
        template += 'overlay_img.html'
    if overlayType == 1:
        template += 'overlay_video.html'

    return render_template(template,
                           name=name,
                           marker_src=targetUri,
                           overlay_src=overlayUri)


def get_data(entity_id):
    conn = mysql.connect()
    cursor = conn.cursor()

    sql_query = f"""SELECT name, targetUri, overlayType, overlayUri 
                    FROM Entities WHERE id = {entity_id};"""

    cursor.execute(sql_query)
    data = cursor.fetchall()
    return data
