with open('AOC-Day01-2021.txt') as f:
    text = f.read()

depths = text.split('\n')

def Day1Part1(file_input):
    count = 0

    for i, depth in enumerate(file_input):

        if i == 0:
            pass
            # print(f'{depth} (start)')
        elif int(depth) > int(file_input[i-1]):
            count += 1
            # print(f'{depth} (increased) count = {count}')
        else:
            # print(f'{depth} (decreased)')
            pass
    print(count)

def Day1Part2(file_input):
    count = 0
    rolling_avg = []
    for i, depth in enumerate(file_input):

        if i == 0 or i == len(file_input)-1:
            pass
        else:
            #print((int(file_input[i-1]) + int(file_input[i]) + int(file_input[i+1]))/3)
            rolling_avg.append((int(file_input[i-1]) + int(file_input[i]) + int(file_input[i+1])))

    return rolling_avg

Day1Part1(depths)
Day1Part1(Day1Part2(depths))


