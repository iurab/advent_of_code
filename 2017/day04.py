import os

def count_valid_passphrases_1(puzzle_input):
    count = 0
    for passphrase in puzzle_input:
        words = passphrase.strip().split()
        if len(words) == len(set(words)):
            count += 1
    return count

def count_valid_passphrases_2(puzzle_input):
    count = 0
    for passphrase in puzzle_input:
        words = passphrase.strip().split()
        map_words = []
        for word in words:
            map_letters = [0] * 26
            letters = list(word)
            for char in letters:
                map_letters[ord(char) - ord('a')] += 1
            unique_text = ''.join(list(map(str,map_letters)))
            map_words.append(unique_text)
        if len(map_words) == len(set(map_words)):
            count += 1
    return count

def get_puzzle_input():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    with open(dir_path + '\\' + 'day4.txt') as file:
        puzzle_input = file.readlines()
    return puzzle_input

def main():
    puzzle_input = get_puzzle_input()
    count_1 = count_valid_passphrases_1(puzzle_input)
    print(count_1)
    count_2 = count_valid_passphrases_2(puzzle_input)
    print(count_2)

if __name__ == '__main__':
    main()