from math import sqrt


def calculate_heuristic(neighbor, end):
    # using the raw distance
    x = (neighbor.x, neighbor.y)
    y = (end.x, end.y)
    distance = sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

