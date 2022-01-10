def get_input():
    with open('input') as file:
        puzzle_input = file.readlines()
    # Just one line
    return puzzle_input[0]


def reacts(x, y):
    # Check is we deal with letters
    if x.isalpha() and y.isalpha():
        return abs(ord(x) - ord(y)) == 32
    return False


def part01(polymer):
    polymer = list(polymer)
    result = []
    for pol in polymer:
        # Array is not empty; Check if the current item and the last item added react
        if result and reacts(pol, result[-1]):
            result.pop()
        else:
            result.append(pol)
    return(len(result))


def part02(polymer):
    # Find all negative items
    negatives = set([item.lower() for item in polymer])
    # Generate all possible lengths and find minimum
    return min([part01(polymer.replace(item, '').replace(item.upper(), '')) for item in negatives])


if __name__ == '__main__':
    polymer = get_input()
    # print(polymer)
    print(part01(polymer))
    print(part02(polymer))