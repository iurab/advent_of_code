import parse
import numpy as np


def get_input():
    claims = []
    matcher = '#{id:d} @ {x:d},{y:d}: {width:d}x{height:d}'
    with open('input') as file:
        puzzle_input = file.read().splitlines()
    for line in puzzle_input:
        r = parse.parse(matcher, line)
        claims.append(r)
    return claims


def part01(claims):
    # Create fabric
    fabric = np.zeros((1000, 1000), dtype=np.int)
    for claim in claims:
        # "Unpack"
        x, y, width, height = claim['x'], claim['y'], claim['width'], claim[
            'height']
        # Select regions and increase values
        fabric[x:x + width, y:y + height] += 1
    overlap = np.sum(np.where(fabric > 1, 1, 0))
    print(overlap)


def part02(claims):
    # Create fabric
    fabric = np.zeros((1000, 1000), dtype=np.int)
    for claim in claims:
        # "Unpack"
        x, y, width, height = claim['x'], claim['y'], claim['width'], claim[
            'height']
        # Select region and increase values
        fabric[x:x + width, y:y + height] += 1
    for claim in claims:
        # "Unpack"
        x, y, width, height = claim['x'], claim['y'], claim['width'], claim[
            'height']
        # Search and see if claim overlaps
        if np.all(fabric[x:x + width, y:y + height] == 1):
            print(claim['id'])
            return


if __name__ == '__main__':
    claims = get_input()
    part01(claims)
    part02(claims)