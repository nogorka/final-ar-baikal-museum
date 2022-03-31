from ..db import mysql_select
import datetime



def get_avg_values_raw():
    sql = """SELECT e.id, e.name,
        vr.visualFeedback, vr.description, vr.completeness
        from entities as e, visitingrecords as vr
        where e.id = vr.entityId;"""
    data = mysql_select(sql)

    stats = {}
    for line in data:
        if line[0] in stats.keys():
            stats[line[0]]['visualFeedback'] += line[2]
            stats[line[0]]['description'] += line[3]
            stats[line[0]]['completeness'] += line[4]
            stats[line[0]]['count'] += 1
        else:
            stats[line[0]] = {'name': line[1],
                              'visualFeedback': line[2],
                              'description': line[3],
                              'completeness': line[4],
                              'count': 1,
                              'avg_total': 0}

    return stats


def get_entities_rating():
    stats = get_avg_values_raw()

    newdata = {}

    for key, st in stats.items():
        st['avg_total'] = (st['visualFeedback'] + st['description'] +
                           st['completeness']) / (3*st['count'])

        newdata[key] = {'name': st['name'],
                        'count': st['count'],
                        'avg_total': round(st['avg_total'], 3)}
    return newdata


def get_rooms_visiting():
    sql = """SELECT e.id, e.name, vr.startTime
        from entities as e, visitingrecords as vr
        where e.id = vr.entityId and
        DATEDIFF(CURDATE(), vr.startTime) = 0;"""
    # datediff показывает разницу
    # между текущей датой и датами, которые есть в бд
    # чтобы посмотреть на не пустой результат
    # нужно изменить значение с 0
    # на количество времени, прошедшее со дня начала

    data = mysql_select(sql)

    stats = {}

    for line in data:
        if line[0] in stats.keys():
            stats[line[0]]['count'] += 1
        else:
            stats[line[0]] = {'name': line[1],
                              'count': 1}
    return stats


def get_avg_values():
    stats = get_avg_values_raw()

    newdata = {}

    for key, st in stats.items():
        st['avg_vis'] = st['visualFeedback'] / st['count']
        st['avg_desc'] = st['description'] / st['count']
        st['avg_comp'] = st['completeness'] / st['count']

        newdata[key] = {'name': st['name'],
                        'avg_vis': round(st['avg_vis'], 3),
                        'avg_desc': round(st['avg_desc'], 3),
                        'avg_comp': round(st['avg_comp'], 3),
                        }
    return newdata


def get_time_spend_in_front():
    sql = """SELECT e.id, e.name, vr.spentTimeSec
        from entities as e, visitingrecords as vr
        where e.id = vr.entityId;"""
    data = mysql_select(sql)

    stats = {}
    for line in data:
        if line[0] in stats.keys():
            stats[line[0]]['timeInFront'].append(line[2])
        else:
            stats[line[0]] = {'name': line[1],
                              'timeInFront': [line[2]]}

    newdata = {}
    for key, st in stats.items():

        newdata[key] = {'name': st['name'],
                        'avg': round(sum(st['timeInFront']) / len(st['timeInFront']), 3),
                        'min':  min(st['timeInFront']),
                        'max':  max(st['timeInFront']),
                        }

    return newdata


def get_weekly():
    sql = """SELECT e.id, e.name, vr.startTime
    from entities as e, visitingrecords as vr
    where e.id = vr.entityId;"""
    data = mysql_select(sql)

    stats = {}

    WEEKDAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    for line in data:
        f = '%Y-%m-%d %H:%M:%S'
        timestamp = line[2].strftime(f)
        day_id = datetime.datetime.strptime(timestamp, f).weekday()

        if line[0] not in stats.keys():
            days = {}
            for name in WEEKDAYS:
                days[name] = 0
            stats[line[0]] = {'name': line[1], 'weekdays': days}

        stats[line[0]]['weekdays'][WEEKDAYS[day_id]] += 1

    newdata = {}
    for _id, ex_line in stats.items():
        ex_line['weekdays']['name'] = ex_line['name']
        newdata[_id] = ex_line['weekdays']

    return newdata
