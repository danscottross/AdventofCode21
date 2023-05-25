"""
from aocd import data
aocd.get_data(day='3', year=2021)
print(aoc_input)
"""

with open('AOC-Day03-2021.txt') as f:
    text = f.read()

def Day3Part1(file_input):
    directions = file_input.split('\n')
    result = [[*line] for line in directions]

    gamma = ''
    epsilon = ''

    for i in range(0, 12):
        zero_count = 0
        one_count = 0

        for line in result:

            if line[i] == '0':
                zero_count += 1
            elif line[i] == '1':
                one_count += 1

        if zero_count > one_count:
            gamma += '0'
            epsilon += '1'

        else:
            gamma += '1'
            epsilon += '0'

        # print(f'0: {zero_count} and 1: {one_count}')

    gamma_decimal = int(gamma, 2)
    epsilon_decimal = int(epsilon, 2)

    solution = gamma_decimal*epsilon_decimal

    print(solution)

def Day3Part2(file_input):
    data = file_input.split('\n')

    o2_list = data
    o2_rating = ''

    for i in range(0, len(o2_list[0])):
        zero_count = 0
        one_count = 0
        for line in o2_list:
            if line[i] == '0':
                zero_count += 1
            elif line[i] == '1':
                one_count += 1

        if zero_count > one_count:
            outcome = '0'
        else:
            outcome = '1'

        o2_list = [line for line in o2_list if line[i] == outcome]

        if len(o2_list) == 1:
            o2_rating = o2_list[0]
            break

    co2_list = data
    co2_rating = ''

    for i in range(0, len(co2_list[0])):
        zero_count = 0
        one_count = 0

        for line in co2_list:
            if line[i] == '0':
                zero_count += 1
            elif line[i] == '1':
                one_count += 1

        if zero_count > one_count:
            outcome = '1'
        else:
            outcome = '0'

        co2_list = [line for line in co2_list if line[i] == outcome]

        if len(co2_list) == 1:
            co2_rating = co2_list[0]
            break

    o2_decimal = int(o2_rating, 2)
    co2_decimal = int(co2_rating, 2)

    solution = o2_decimal*co2_decimal

    print('o2_rating: ', o2_rating)
    print('o2_decimal: ', o2_decimal)
    print('co2_rating: ', co2_rating)
    print('co2_decimal: ', co2_decimal)
    print('solution: ', solution)

# Day3Part1(text)
Day3Part2(text)
