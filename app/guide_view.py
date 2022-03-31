from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .logic.route_building import build_route, get_directions, parse_route_direct
from .db import mysql_select

guide = Blueprint('guide', __name__)


@guide.route('/route')
def route():

    depart = request.args.get('depart')
    dest = request.args.get('dest')

    route = get_directions(depart, dest)
    msg_route = parse_route_direct(route).capitalize()
    name = f"Путь от {depart} до {dest}"

    sql = f"""SELECT name, targetUri, overlayType, overlayUri 
                    FROM Entities WHERE id = {dest};"""
    data = mysql_select(sql)

    if data:
        _, targetUri, overlayType, overlayUri = data[0]

        return render_template('guide_nav/route_message.html', name=name, message=msg_route, marker_src=targetUri)

    msg_route += " Для завершения экскурсии наведите повторно на последний экспонат."
    return render_template('guide_nav/route_message.html', name=name, message=msg_route, marker_src="assets/markers/zpt/9.zpt")


@guide.route('/show/<entity_id>')
def show(entity_id):

    sql = f"""SELECT name, targetUri, overlayType, overlayUri 
                    FROM Entities WHERE id = {entity_id};"""
    data = mysql_select(sql)

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
