from itertools import permutations

def get_input():
    # Get data
    with open('input') as file:
        data = file.read().splitlines()
    # Adapt / convert information
    expenses = list(map(int, data))
    return expenses

def part01(expenses):
    # Find the 2 entries for which the sum = 2020
    for x, y in permutations(expenses,2):
        if x + y == 2020:
            # Print the product of those values
            print(x * y)
            break

def part02(expenses):
    # Find the 3 entries for which the sum = 2020
    for x, y, z in permutations(expenses,3):
        if x + y  + z == 2020:
            # Print the product of those values
            print(x * y * z)
            break

if __name__ == '__main__':
    expenses = get_input()
    part01(expenses)
    part02(expenses)