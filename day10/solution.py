from copy import deepcopy
from math import inf

def parse_input(input):
    points = []
    for point_line in input:
        pos_x = int(point_line.split("<")[1].split(",")[0])
        pos_y = int(point_line.split("<")[1].split(",")[1].split(">")[0])
        velocity_x = int(point_line.split("<")[2].split(",")[0])
        velocity_y = int(point_line.split("<")[2].split(",")[1].split(">")[0])
        points.append(([pos_x, pos_y], (velocity_x, velocity_y)))
    return points

def elapse_time(points, num_seconds):
    for point in points:
        point[0][0] += point[1][0] * num_seconds
        point[0][1] += point[1][1] * num_seconds

def calculate_height(points):
    return max(points, key=lambda x: x[0][1])[0][1] - min(points, key=lambda x: x[0][1])[0][1] + 1

def compose_message(points):
    min_x = min(points, key=lambda x: x[0][0])[0][0]
    max_x = max(points, key=lambda x: x[0][0])[0][0]
    min_y = min(points, key=lambda x: x[0][1])[0][1]
    max_y = max(points, key=lambda x: x[0][1])[0][1]
    message = "\n"
    for y in range(min_y, max_y + 1):
        line = ["."] * (max_x + 1 - min_x)
        for point in points:
            if point[0][1] == y:
                line[point[0][0] - min_x] = "#"
        message = "".join([message, "".join(line), "\n"])
    return message

def elapse_until_message(points):
    original_points = deepcopy(points)
    last_height = inf
    current_height = calculate_height(points)
    elapsed_time = 0
    while current_height < last_height:
        elapse_time(points, 1)
        elapsed_time += 1
        last_height = current_height
        current_height = calculate_height(points)
    points = original_points
    elapse_time(points, elapsed_time - 1)
    return (compose_message(points), elapsed_time - 1)

def first_star(input):
    points = parse_input(input)
    return elapse_until_message(points)[0]

def second_star(input):
    points = parse_input(input)
    return elapse_until_message(points)[1]