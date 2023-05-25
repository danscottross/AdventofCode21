from collections import Counter

with open('AOC-Day05-2021.txt') as f:
    data = f.read().splitlines()

# coordinates = [[[int(value) for value in pair.split(',')] for pair in line.split(' -> ')] for line in init_input]

def extract_points_part1(coordinate_list, notation='string'):
    master_list = []
    for line in coordinate_list:
        first_point, second_point = line.split('->')
        x1, y1 = tuple(map(int, first_point.split(',')))
        x2, y2 = tuple(map(int, second_point.split(',')))

        # Vertical lines
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                master_list.append((x1, y))

        # Horizontal lines
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                master_list.append((x, y1))

    return master_list

def extract_points_part2(coordinate_list):
    master_list = []
    for line in coordinate_list:
        first_point, second_point = line.split('->')
        x1, y1 = tuple(map(int, first_point.split(',')))
        x2, y2 = tuple(map(int, second_point.split(',')))

        # Vertical lines
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                master_list.append((x1, y))

        # Horizontal lines
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                master_list.append((x, y1))

        else:
            x_inc = 1 if x1 < x2 else -1
            y_inc = 1 if y1 < y2 else -1
            y = y1
            x = x1
            for x in range(x1, x2 + x_inc, x_inc):
                master_list.append((x, y))
                y += y_inc

    return master_list

def final_answer(input_list):
    tabulated_list = dict(Counter(input_list))
    # print(tabulated_list)
    intersections = [key for key, value in tabulated_list.items() if value > 1]
    print(len(intersections))

final_answer(extract_points_part1(data))
final_answer(extract_points_part2(data))



"""

FIRST ATTEMPT, did not capture all intercepts

def extract_points2(coordinate_list, notation='string'):
    master_list = []
    for line in coordinate_list:
        first_point, second_point = line.split('->')

        # horizontal line (y1 = y2)
        if pair[0][1] == pair[1][1]:
            y_coord = pair[0][1]
            for step in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0]) + 1):
                if notation == 'string':
                    master_list.append(f'{step}x{y_coord}y')
                else:
                    master_list.append([step, y_coord])

        # vertical line (x1 = x2)
        if pair[0][0] == pair[1][0]:
            x_coord = pair[0][0]
            for step in range(min(pair[0][1], pair[1][1]), min(pair[0][1], pair[1][1]) + 1):
                if notation == 'string':
                    master_list.append(f'{x_coord}x{step}y')
                else:
                    master_list.append([step, x_coord])

        else:
            pass

    return master_list


    return master_list

import pandas as pd
from collections import Counter

def part1(input_list):
    points_list = extract_points(input_list)
    tabulated_list = dict(Counter(points_list))
    print(tabulated_list)
    intersections = [key for key, value in tabulated_list.items() if value > 1]
    print(len(intersections))

part1(coordinates)
"""


