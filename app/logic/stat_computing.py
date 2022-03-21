from ..db import mysql


def get_data(sql_query):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(sql_query)
    return cursor.fetchall()


def get_entities_rating():
    sql = """SELECT e.id, e.name, 
        vr.visualFeedback, vr.description, vr.completeness 
        from entities as e, visitingrecords as vr 
        where e.id = vr.entityId;"""
    data = get_data(sql)

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
                              "description": line[3],
                              "completeness": line[4],
                              'count': 1,
                              'avg_total': 0}

    newdata = {}

    for key, st in stats.items():
        st['avg_total'] = (st['visualFeedback'] + st['description'] +
                           st['completeness']) / (3*st['count'])

        newdata[key] = {'name': st['name'],
                        'count': st['count'],
                        'avg_total': round(st['avg_total'], 3)}
    return newdata


def get_rooms_visiting():
    sql = """SELECT e.id, e.name, 
        vr.visualFeedback, vr.description, vr.completeness 
        from entities as e, visitingrecords as vr 
        where e.id = vr.entityId;"""
    data = get_data(sql)

    stats = {}
    return stats
