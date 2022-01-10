def get_input():
    patterns, numbers = [], []
    with open("input") as file:
        lines = file.readlines()
        for line in lines:
            pattern, number = line.strip().split(" | ")
            patterns.append(pattern.split(" "))
            numbers.append(number.split(" "))
    return (patterns, numbers)


def part01(numbers):
    lengths = [len(digit) for number in numbers for digit in number]
    uniques = [2, 3, 4, 7]
    nr_uniques = sum(lengths.count(unique) for unique in uniques)
    print(nr_uniques)


def part02(patterns, numbers):
    # Definitions
    dashes_to_digit = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    sum_nr = 0

    for i, pattern in enumerate(patterns):
        # Replace map
        replace_map = {}
        # Find digit: 1
        one = list(filter(lambda x: len(x) == 2, pattern))[0]
        seven = list(filter(lambda x: len(x) == 3, pattern))[0]
        four = list(filter(lambda x: len(x) == 4, pattern))[0]
        eight = list(filter(lambda x: len(x) == 7, pattern))[0]
        dash_top_mid = list(set(list(seven)) - set(list(one)))[0]
        replace_map[dash_top_mid] = "a"
        # Get all differences between 8 and 0,6,9
        diff = []
        for scrambled_digit in list(filter(lambda x: len(x) == 6, pattern)):
            diff.append(list(set(list(eight)) - set(list(scrambled_digit)))[0])
        for dash in diff:
            if dash in one:
                replace_map[dash] = "c"
            elif dash in four:
                replace_map[dash] = "d"
            else:
                replace_map[dash] = "e"
        # Map missing dash from one
        for dash in one:
            if dash not in replace_map:
                replace_map[dash] = "f"
                break
        # Map missing dash from four
        for dash in four:
            if dash not in replace_map:
                replace_map[dash] = "b"
                break
        # Map missing dash from eight
        for dash in eight:
            if dash not in replace_map:
                replace_map[dash] = "g"
        # Correct pattern / circuit
        number = []
        for scrambled_digit in numbers[i]:
            dashes = []
            for dash in scrambled_digit:
                dashes.append(replace_map[dash])
            number_digit = dashes_to_digit["".join(sorted(dashes))]
            number.append(number_digit)
        sum_nr += int("".join(number))
    print(sum_nr)


if __name__ == "__main__":
    patterns, numbers = get_input()
    part01(numbers)
    part02(patterns, numbers)
