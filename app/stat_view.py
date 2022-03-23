from flask import Blueprint, render_template, request, redirect, url_for, jsonify
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


@stat.route('/time_in_front_data')
def time_in_front_data():
    data = get_time_spend_in_front()
    return jsonify(data=data)


@stat.route('/avg_values_data')
def avg_values_data():
    data = get_avg_values()
    return jsonify(data=data)


@stat.route('/time_in_front')
def time_in_front():
    return render_template("chart.html",
                           url="/time_in_front_data",
                           chart_label="Time spent in front",
                           xlabel="entities",
                           ylabel="views amount in sec",
                           description="""Отображение средней, минимальной 
                            и максимальной оценки времени, 
                            которое пользователь провел перед экспонатом.""")


@stat.route('/avg_values')
def avg_values():
    return render_template("chart.html",
                           url="/avg_values_data",
                           chart_label="Average values",
                           xlabel="entities",
                           ylabel="visiting amount",
                           description="""Отображение для каждого экспоната 
                           **средних оценок** пользователей отдельно 
                           по каждому из критериев:
                                1. визуальная составляющая;
                                2. описание экспоната;
                                3. законченность образа.""")


@stat.route('/weekly')
def weekly():
    return "weekly"
