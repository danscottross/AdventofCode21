from collections import Counter
import numpy as np
import math

with open('AOC-Day07-2021.txt') as f:
    data = list(map(int, f.read().split(',')))

def crab_median(input_list):
    return round(np.median(input_list))

def fuel_calc(input_list, med):
    fuel = 0
    for crab in input_list:
        fuel += abs(crab-med)
    print(fuel)

def crab_avg_ceil(input_list):
    ceil = math.ceil(np.average(input_list))
    return ceil

def crab_avg_floor(input_list):
    floor = math.floor(np.average(input_list))
    return floor

def fuel_calc_exp(input_list, avg):
    fuel = 0
    for crab in input_list:
        n = abs(crab-avg)
        fuel += sum(range(abs(crab-avg)+1))
    print(f"Position: {avg} || Fuel Consumption: {fuel}")

fuel_calc(data, crab_median(data))
fuel_calc_exp(data, crab_avg_floor(data))
fuel_calc_exp(data, crab_avg_ceil(data))
