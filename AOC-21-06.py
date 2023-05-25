from collections import Counter

with open('AOC-Day06-2021.txt') as f:
    data = list(map(int, f.read().split(',')))

def lantern_population(fish_list, days):
    for day in range(days):
        for i, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[i] = 7
                fish_list.append(9)
            fish_list[i] -= 1

    print(len(fish_list))

def large_lantern_population(fish_list, days):
    fish_dict = dict(Counter(fish_list))
    for day in range(days):
        output_dict = {}
        merge = 0
        for fish_age, count in fish_dict.items():
            if fish_age == 0:
                output_dict[8] = count
                merge += count
            elif fish_age == 7:
                merge += count
            else:
                output_dict[fish_age - 1] = count
        output_dict[6] = merge
        fish_dict = output_dict

    print(fish_dict)
    print(sum(fish_dict.values()))

large_lantern_population(data, 0)
large_lantern_population(data, 1)
large_lantern_population(data, 2)
large_lantern_population(data, 3)
large_lantern_population(data, 4)
large_lantern_population(data, 256)

