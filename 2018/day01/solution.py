import os
import itertools


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '/' + 'input') as file:
        puzzle_input = file.readlines()
    return puzzle_input


def part1(freq_changes):
    # Calculate resulting frequency
    frequency = sum([int(value) for value in freq_changes])
    print(frequency)


def part2(freq_changes):
    # Find the first frequency to repeat
    all_frequencies = set([0])
    freq = 0
    for value in itertools.cycle(freq_changes):
        freq += int(value)
        if freq in all_frequencies:
            print(freq)
            return
        all_frequencies.add(freq)


if __name__ == '__main__':
    puzzle_input = get_puzzle_input()
    part1(puzzle_input)
    part2(puzzle_input)
