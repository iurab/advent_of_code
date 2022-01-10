import day10


def make_grid(key):
    grid = []
    for i in range(128):
        hash_ = day10.knot_hash_2('{}-{}'.format(key, i))
        grid.append('{:#0130b}'.format(int(
            hash_, 16))[2:])  # "#0130" to zero pad; 128 digits plus leading 0b
    return grid


def part1(key):
    grid = make_grid(key)
    return ''.join(grid).count('1')


def part2(key):
    # Convert grid to set of coordinates
    grid = {(i, j)
            for i, row in enumerate(make_grid(key))
            for j, ch in enumerate(row)
            if ch == '1'}
    regions = 0
    while grid:
        regions += 1
        new = [grid.pop()]  # Check random region
        while new:
            old = new.copy()
            new = []
            for x, y in old:
                for pair in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if pair in grid:
                        grid.remove(pair)
                        new.append(pair)
    return regions


solution1 = part1('jzgqcdpd')
print(solution1)
solution2 = part2('jzgqcdpd')
print(solution2)
