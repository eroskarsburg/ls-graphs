"""Funções auxiliares para o projeto"""

import math


def haversine(lat1, lon1, lat2, lon2):
    """Calcula a distância, em metros, entre duas coordenadas GPS."""
    dLat = (lat2 - lat1) * math.pi / 180.0  # pylint: disable=invalid-name
    dLon = (lon2 - lon1) * math.pi / 180.0  # pylint: disable=invalid-name
    # convert to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
    # apply formulae
    a = (
        pow(math.sin(dLat / 2), 2) +
        pow(math.sin(dLon / 2), 2) *
        math.cos(lat1) * math.cos(lat2)
    )
    rad = 6371
    c = 2 * math.asin(math.sqrt(a))
    return (rad * c)*1000


#
# Não altere este comentário e adicione suas funções ao final do arquivo.
#

def heuristic(node, goal_node):
    x1, y1 = float(node[0][0]), float(node[0][1])
    x2, y2 = float(goal_node[0][0]), float(goal_node[0][1]) 
    val = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return val  # Euclidean distance