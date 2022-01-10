import re

def is_increasing(number: str):
    return ''.join(sorted(number)) == number

def has_two(number: str):
    return re.search(r'(\d)\1+', number) is not None

def has_exactly_two(number: str):
    return any(len(match.group(0)) == 2 for match in re.finditer(r'(\d)\1+', number))


def part01():
    count = 0
    for i in range(193651, 649729 + 1):
        number = str(i)
        count += 1 if is_increasing(number) and has_two(number) else 0
    print(count)

def part02():
    count = 0
    for i in range(193651, 649729 + 1):
        number = str(i)
        count += 1 if is_increasing(number) and has_exactly_two(number) else 0
    print(count)

if __name__ == '__main__':
    part01()
    part02()