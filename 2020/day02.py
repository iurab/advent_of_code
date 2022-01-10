def get_input():
    with open('input') as file:
        lines = file.readlines()
    return lines    

def part01(lines):
    valid = 0
    for line in lines:
        entries = line.split(' ')
        low, high = list(map(int, entries[0].split('-')))
        letter = entries[1][0]
        password = entries[2].strip()
        if low <= password.count(letter) <= high:
            valid += 1
    print(valid)

def part02(lines):
    valid = 0
    for line in lines:
        entries = line.split(' ')
        pos1, pos2 = list(map(int, entries[0].split('-')))
        letter = entries[1][0]
        password = entries[2].strip()
        if (password[pos1-1] == letter) ^ (password[pos2-1] == letter):
            valid += 1
    print(valid)

if __name__ == '__main__':
    lines = get_input()
    part01(lines)
    part02(lines)