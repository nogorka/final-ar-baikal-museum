from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from .logic.stat_computing import get_entities_rating, get_rooms_visiting
from .logic.stat_computing import get_time_spend_in_front, get_avg_values, get_weekly
stat = Blueprint('stat', __name__)


@stat.route('/statistics')
def statistics_menu():
    return render_template('stat/statistics.html')


@stat.route('/rooms_visiting')
def rooms_visiting():
    data = get_rooms_visiting()
    head, msg = list(), ''
    if data:
        head = list(data.values())[0].keys()
    else:
        msg = 'В данный момент в залах никого нет'

    return render_template('stat/list.html',
                           data=data,
                           thead=head,
                           name='Посещаймость залов',
                           description="""Посещения по залам в течение дня 
                           (данные есть только на время проведения мероприятия 7-12 марта)""",
                           msg=msg)


@stat.route('/entities_rating')
def entities_rating():
    data = get_entities_rating()
    head = list(data.values())[0].keys()
    return render_template('stat/list.html',
                           data=data,
                           thead=head,
                           name='Рейтинг экспонатов',
                           description="""Общий список экспонатов по посещаемости 
                           и по средней общей оценке""",
                           msg='')


@stat.route('/time_in_front_data')
def time_in_front_data():
    data = get_time_spend_in_front()
    return jsonify(data=data)


@stat.route('/avg_values_data')
def avg_values_data():
    data = get_avg_values()
    return jsonify(data=data)


@stat.route('/weekly_data')
def weekly_data():
    data = get_weekly()
    return jsonify(data=data)


@stat.route('/time_in_front')
def time_in_front():
    return render_template('stat/chart.html',
                           url='/time_in_front_data',
                           chart_label='Оценка потраченного времени (сек)',
                           xlabel='Экспонаты',
                           ylabel='Время потраченное (сек)',
                           description="""Отображение средней, минимальной 
                            и максимальной оценки времени, 
                            которое пользователь провел перед экспонатом.""")


@stat.route('/avg_values')
def avg_values():
    return render_template('stat/chart.html',
                           url='/avg_values_data',
                           chart_label='Средние оценки по критериям',
                           xlabel='Экспонаты',
                           ylabel='Оценка',
                           description="""Отображение для каждого экспоната 
                           **средних оценок** пользователей отдельно 
                           по каждому из критериев:
                                1. визуальная составляющая;
                                2. описание экспоната;
                                3. законченность образа.""")


@stat.route('/weekly')
def weekly():
    return render_template('stat/chart.html',
                           url='/weekly_data',
                           chart_label='Посещение по дням недели',
                           xlabel='День недели',
                           ylabel='Количество посещений',
                           description="""Отображение графика посещения всех 
                           экспонатов в зависимости от дня недели.""")
