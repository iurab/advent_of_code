import os
import collections


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '/' + 'input') as file:
        puzzle_input = file.read().splitlines()
    return puzzle_input

def part01(box_ids):
    rep_02 = 0
    rep_03 = 0
    for id in box_ids:
        characters = collections.Counter(id)
        rep_02 += any([True if count == 2 else False for _, count in characters.items()])
        rep_03 += any([True if count == 3 else False for _, count in characters.items()])
    print(rep_02 * rep_03)

def part02(box_ids):
    for i in range(len(box_ids)):
        for j in range(i + 1, len(box_ids)):
            id_a = list(box_ids[i])
            id_b = list(box_ids[j])
            diffs = [True if id_a[pos] != id_b[pos] else False for pos in range(len(id_a))]
            if sum(diffs) == 1:
                id_a.pop(diffs.index(True))
                print(''.join(id_a))
                return


if __name__ == '__main__':
    puzzle_input = get_puzzle_input()
    part01(puzzle_input)
    part02(puzzle_input)
