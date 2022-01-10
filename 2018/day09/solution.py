from parse import parse
from collections import deque


def get_input():
    matcher = "{n_players:d} players; last marble is worth {n_points:d} points"
    line = open("input").read()
    values = parse(matcher, line)
    return values


def part01(values):
    scores = [0 for _ in range(values["n_players"])]
    circle = deque([0])
    for marble in range(1, values['n_points'] + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % len(scores)] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble) 
    print(max(scores))

if __name__ == "__main__":
    values = get_input()
    part01(values)