import os
from functools import reduce
from operator import ixor


def knot_hash_1(puzzle_input):
    # Define first values [0, ..., 255]
    rope = list(range(0, 256))
    # Define initial values
    skip_size = 0
    position = 0
    # Parse
    for knot in puzzle_input:
        selection = [
            i if i < 256 else i % 256 for i in range(position, position + knot)
        ]
        selection_values = [rope[sel] for sel in selection]
        # Rervese the selection
        selection_values = selection_values[::-1]
        for idx, sel in enumerate(selection):
            rope[sel] = selection_values[idx]
        position += knot + skip_size
        skip_size += 1

    print(rope)
    print('Hash', rope[0] * rope[1])


def knot_hash_2(puzzle_input):
    # Create length sequence
    length_seq = list(map(ord, list(puzzle_input)))
    length_seq += [17, 31, 73, 47, 23]
    # Define first values [0, ..., 255]
    rope = list(range(0, 256))
    # Define initial values
    skip_size = 0
    position = 0
    # Generate SPARSE hash
    for _ in range(64):
        for knot in length_seq:
            selection = [
                i if i < 256 else i % 256
                for i in range(position, position + knot)
            ]
            selection_values = [rope[sel] for sel in selection]
            # Rervese the selection
            selection_values = selection_values[::-1]
            for idx, sel in enumerate(selection):
                rope[sel] = selection_values[idx]
            position += knot + skip_size
            skip_size += 1
    # Generate DENSE hash
    dense_hash = []
    for i in range(16):
        start_pos = i * 16
        xor_element = reduce(ixor, rope[start_pos:start_pos + 16])
        dense_hash.append(xor_element)
    dense_has_hex = []
    for int_has in dense_hash:
        dense_has_hex.append('{0:02x}'.format(int_has))
    # print(''.join(dense_has_hex))
    return ''.join(dense_has_hex)


def get_puzzle_input_1():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '/' + 'day10.txt') as file:
        raw_input = file.read()
    puzzle_input = list(map(int, raw_input.strip().split(',')))
    return puzzle_input


def get_puzzle_input_2():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '/' + 'day10.txt') as file:
        raw_input = file.read()
    puzzle_input = raw_input.strip()
    return puzzle_input


def main():
    puzzle_input = get_puzzle_input_1()
    knot_hash_1(puzzle_input)
    puzzle_input = get_puzzle_input_2()
    knot_hash_2(puzzle_input)


if __name__ == '__main__':
    main()
