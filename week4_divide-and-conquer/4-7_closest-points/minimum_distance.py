from collections import namedtuple
from itertools import combinations
from math import sqrt

Point = namedtuple('Point', 'x y')

# Naive

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def minimum_distance_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return sqrt(min_distance_squared)


def minimum_distance(points):
    points.sort()
    return get_closest_distance(points)

def get_closest_distance(points):
    size = len(points)

    if size < 10:
        return minimum_distance_naive(points)
    
    left_side = points[:size // 2]
    right_side = points[size // 2:]
    
    left_distance = get_closest_distance(left_side)
    right_distance = get_closest_distance(right_side)
    
    min_distance = min(left_distance, right_distance)
    
    if min_distance == 0.0:
        return min_distance
    
    median = (left_side[-1][0] + right_side[0][0]) / 2
    
    sigmas = []
    
    for s in range(len(left_side)):
        if abs(left_side[s][0] - median) < min_distance:
            sigmas.append(left_side[s])
    for s in range(len(right_side)):
        if abs(right_side[s][0] - median) < min_distance:
            sigmas.append(right_side[s])
            
    sigmas.sort(key=lambda y: y[1])
    
    for s in range(len(sigmas) - 1):
        for t in range (s + 1, min(s + 6, len(sigmas))):
            if abs(sigmas[s][1] - sigmas[t][1] < min_distance):
                min_distance = min(min_distance, sqrt(distance_squared(sigmas[s], sigmas[t])))
    
    return min_distance


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    print("{0:.9f}".format((minimum_distance(input_points))))
