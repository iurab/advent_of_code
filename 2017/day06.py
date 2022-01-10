import os

def memory_reallocation_1(blocks):
    prevs = []
    while blocks not in prevs:
        prevs.append(blocks[:])
        max_memory = max(blocks)
        position = blocks.index(max_memory)
        blocks[position] = 0
        while max_memory:
            position = (position + 1) % len(blocks)
            blocks[position] += 1
            max_memory -= 1
    print(len(prevs))
    print(len(prevs)-prevs.index(blocks))


def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '\\' + 'day6.txt') as file:
        raw_input = file.read()
    puzzle_input = list(map(int, raw_input.strip().split()))
    return puzzle_input

def main():
    puzzle_input = get_puzzle_input()
    memory_reallocation_1(puzzle_input)
    #solution_from_online(puzzle_input)

if __name__ == '__main__':
    main()
