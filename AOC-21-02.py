with open('AOC-Day02-2021.txt') as f:
    text = f.read()

def Day2Part1(file_input):
    directions = file_input.split('\n')
    split_directions = [line.split() for line in directions]

    x = 0
    y = 0

    for move in split_directions:
        direction = move[0]
        distance = move[1]

        if direction == 'forward':
            x += int(distance)
        elif direction == 'down':
            y += int(distance)
        elif direction == 'up':
            y -= int(distance)
        else:
            print('ERROR')

    solution = x*y
    print(solution)

Day2Part1(text)

def Day2Part2(file_input):
    directions = file_input.split('\n')
    split_directions = [line.split() for line in directions]

    x = 0
    y = 0
    aim = 0

    for move in split_directions:
        direction = move[0]
        distance = move[1]

        if direction == 'forward':
            x += int(distance)
            y += int(distance)*aim
        elif direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)
        else:
            print('ERROR')

    solution = x*y
    print(solution)

Day2Part2(text)