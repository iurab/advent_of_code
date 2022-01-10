from collections import defaultdict
from intcode import IntCode


class Robot:

    moves = {'^': [0, -1], '<': [-1, 0], 'v': [0, 1], '>': [1, 0]}

    def __init__(self):
        self.orientation = '^'

    def next_move(self, turn):
        # 0 - LEFT
        # 1 - RIGHT
        if self.orientation == '^':
            self.orientation = '<' if turn == 0 else '>'
        elif self.orientation == '<':
            self.orientation = 'v' if turn == 0 else '^'
        elif self.orientation == 'v':
            self.orientation = '>' if turn == 0 else '<'
        elif self.orientation == '>':
            self.orientation = '^' if turn == 0 else 'v'
        return self.moves[self.orientation]


def get_input():
    with open('input') as file:
        line = file.readline().split(',')
    data = defaultdict(int)
    for pos, x in enumerate(line):
        data[pos] = int(x)
    return data


def part01():
    opcodes = get_input()
    computer = IntCode(opcodes)
    canvas = defaultdict(int)
    position = [0, 0]
    robot = Robot()
    while computer.done == False:
        x,y = position
        current_color = canvas[(x,y)]
        computer.set_input(current_color)
        new_color = computer.run()
        turn = computer.run()
        if not computer.done:
            canvas[(x,y)] = new_color
            next_move = robot.next_move(turn)
            position = [x + y for x, y in zip(position, next_move)]
    print(len(canvas))


def part02():
    opcodes = get_input()
    computer = IntCode(opcodes)
    canvas = { (0, 0): 1 }
    position = [0, 0]
    robot = Robot()
    while computer.done == False:
        x,y = position
        computer.set_input(canvas[(x, y)] if (x, y) in canvas else 0)
        new_color = computer.run()
        turn = computer.run()
        if not computer.done:
            canvas[(x,y)] = new_color
            next_move = robot.next_move(turn)
            position = [x + y for x, y in zip(position, next_move)]

    # Build registration
    registration = [[' '] * 40 for _ in range(6)]
    for row in range(6):
        for col in range(40):
            if (col, row) in canvas and canvas[(col, row)] == 1:
                registration[row][col] = '*'
    text = '\n'.join(''.join(row) for row in registration)
    print(text)


part01()
part02()