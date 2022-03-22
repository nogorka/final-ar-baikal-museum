from flask import Blueprint, render_template, request, redirect, url_for
from .db import mysql
from .logic.stat_computing import get_entities_rating, get_rooms_visiting
main = Blueprint('main', __name__)


@main.route('/')
def welcome():
    return render_template('welcome.html')


@main.route('/guide')
def guide():
    return render_template('start_page.html')


@main.route('/photobooth')
def photobooth():
    return "photobooth"


@main.route('/gallery')
def gallery():
    return 'gallery'


@main.route('/portal')
def portal():
    return 'portal'


@main.route('/statistics')
def statistics_menu():
    return render_template('statistics.html')


@main.route('/rooms_visiting')
def rooms_visiting():
    data = get_rooms_visiting()
    head = list(data.values())[0].keys()
    return render_template('list.html',
                           data=data,
                           thead=head,
                           name="Посещаймость залов",
                           description="""Посещения по залам в течение дня """)


@main.route('/entities_rating')
def entities_rating():
    data = get_entities_rating()
    head = list(data.values())[0].keys()
    return render_template('list.html',
                           data=data,
                           thead=head,
                           name="Рейтинг экспонатов",
                           description="""Общий список экспонатов по посещаемости 
                           и по средней общей оценке""")
