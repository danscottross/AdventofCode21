"""
from aocd import data
aocd.get_data(day='3', year=2021)
print(aoc_input)
"""

with open('AOC-Day04-1-2021.txt') as f:
    numbers = f.read()

numbers_list = numbers.split(',')

with open('AOC-Day04-2-2021.txt') as f:
    boards = f.read()

def setup(file_input):
    file_input = file_input.replace('  ', ' ')
    boards_list = [board for board in file_input.split('\n\n')]
    boards_list = [[[int(value) for value in line.split()] for line in board.split('\n')] for board in boards_list]

    return boards_list

winning_column_board = [[['X', 0, 0, 0, 0], ['X', 0, 0, 0, 0], ['X', 0, 0, 0, 0], ['X', 0, 0, 0, 0], ['X', 0, 0, 0, 0]]]
winning_row_board = [[['X', 'X', 'X', 'X', 'X'], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]

def row_check(game_boards):
    row_winner = False
    for board in game_boards:
        for line in board:
            count = 0
            for value in line:
                if value == 'X':
                    count += 1
            if count == 5:
                row_winner = True
        if row_winner:
            print('Row Winner')
            return True

def column_check(game_boards):
    column_winner = False
    for board in game_boards:
        col_index = 0
        while col_index < 5:
            count = 0
            for line in board:
                if line[col_index] == 'X':
                    count += 1
                if count == 5:
                    column_winner = True
                    break
            col_index += 1

        if column_winner:
            print('Column Winner')
            return True

def play_bingo(balls, cards):
    for number in balls:
        for card in cards:
            for line in card:
                for i, value in enumerate(line):
                    if value[i] == number:
                        value[i] = 'X'

        if column_check(cards):
            return card

        if row_check(cards):
            return card

bingo_cards = setup(boards)
play_bingo(numbers_list, bingo_cards)

#column_check(winning_column_board)
#column_check(winning_row_board)
#row_check(winning_column_board)
#row_check(winning_row_board)