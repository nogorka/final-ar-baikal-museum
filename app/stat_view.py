from flask import Blueprint, render_template, request, redirect, url_for
from .logic.stat_computing import get_entities_rating, get_rooms_visiting, get_time_spend_in_front, get_avg_values
stat = Blueprint('stat', __name__)


@stat.route('/statistics')
def statistics_menu():
    return render_template('statistics.html')


@stat.route('/rooms_visiting')
def rooms_visiting():
    data = get_rooms_visiting()
    head, msg = list(), ""
    if data:
        head = list(data.values())[0].keys()
    else:
        msg = "В данный момент в залах никого нет"

    return render_template('list.html',
                           data=data,
                           thead=head,
                           name="Посещаймость залов",
                           description="""Посещения по залам в течение дня 
                           (данные есть только на время проведения мероприятия 7-12 марта)""",
                           msg=msg)


@stat.route('/entities_rating')
def entities_rating():
    data = get_entities_rating()
    head = list(data.values())[0].keys()
    return render_template('list.html',
                           data=data,
                           thead=head,
                           name="Рейтинг экспонатов",
                           description="""Общий список экспонатов по посещаемости 
                           и по средней общей оценке""",
                           msg="")


@stat.route('/time_in_front')
def time_in_front():
    data = get_time_spend_in_front()
    print(data)
    return "time in front"


@stat.route('/avg_values')
def avg_values():
    data = get_avg_values()
    print(data)
    return "avg values"


@stat.route('/weekly')
def weekly():
    return "weekly"
