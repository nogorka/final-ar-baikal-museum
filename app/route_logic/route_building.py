from ..db import mysql
import json
import networkx as nx
import matplotlib.pyplot as plt
import random


def get_route_json():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT jsonUri from map;")
    uri = cursor.fetchall()[0][0]
    return uri


def open_json(path):
    with open(path) as f:
        matrix = json.load(f)
        return matrix


def build_graph():

    matrix = open_json(get_route_json())

    G = nx.Graph()
    edges = []
    def_nodes = []

    for departureEx, destinationsEx in matrix.items():
        def_nodes.append(departureEx)

        for dest in destinationsEx.keys():
            edges.append((departureEx, dest))

    G.add_nodes_from(def_nodes)
    G.add_edges_from(edges)

    return G


def plan_route(route_str):
    graph = build_graph()
    nodes = route_str.split(',')

    if '0' not in nodes:            # add starting point
        nodes.append('0')

    nodes.sort()

    return nx.approximation.traveling_salesman_problem(graph, nodes=nodes)


def build_route(data):  # return list

    if data['type'] == "predefined" or data['type'] == "custom":
        route = plan_route(data['route'])

    elif data['type'] == "generated":
        amount = random.randint(3, 9)
        nodes = set(str(random.randrange(1, 9, 1)) for i in range(amount))
        nodes_str = ','.join(nodes)

        route = plan_route(nodes_str)

    else:
        route = None

    return route
