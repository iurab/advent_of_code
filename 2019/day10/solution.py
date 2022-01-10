from math import atan2, degrees
from collections import OrderedDict
from itertools import cycle


class Asteroid:
    def __init__(self, astr_map, position):
        self.astr_map = astr_map[:]
        self.position = position

    def analyze(self):
        self.visible = {}  # angle: asteroid position
        for y in range(len(self.astr_map)):
            for x in range(len(self.astr_map[y])):
                # Not an asteroid
                if self.astr_map[y][x] == '.':
                    continue
                # Self
                if self.position == (x, y):
                    continue
                pos_x, pos_y = self.position
                angle = degrees(atan2(y - pos_y, x - pos_x))
                if angle not in self.visible:
                    self.visible[angle] = [(x, y)]
                else:
                    self.visible[angle].append((x, y))

    def visible_asteroids(self):
        return len(self.visible)

    def angles_clockwise(self):
        ranges = [(-90, 0), (0, 90), (90, 180), (-180, -90)]
        quarters = []
        for i in range(len(ranges)):
            quarters.append({})
            for angle in self.visible:
                if ranges[i][0] <= angle < ranges[i][1]:
                    quarters[i][angle] = self.visible[angle]
        self.visible = OrderedDict()
        for i in range(len(ranges)):
            for entry in sorted(quarters[i]):
                self.visible[entry] = quarters[i][entry]

    def distance(self, pos1, pos2):
        return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

    def sort_distance_astr(self):
        for angle in self.visible:
            self.visible[angle].sort(
                key=lambda aster_pos: self.distance(self.position, aster_pos))

    def blast(self):
        for angle in cycle(self.visible.keys()):
            yield self.visible[angle].pop(0)

    def vaporize(self):
        # Reorder the angle to start from -90 (UP) and go clockwise
        self.angles_clockwise()
        # Sort asteroids by distance
        self.sort_distance_astr()
        # Start to blast asteroids
        count = 1
        for pos in self.blast():
            count += 1
            if count == 200:
                print(pos)
                break


def get_input():
    with open('input') as file:
        lines = file.readlines()

    data = [list(line.strip()) for line in lines]
    return data


def part01():
    asteroids = []
    astr_map = get_input()
    for y in range(len(astr_map)):
        for x in range(len(astr_map[y])):
            if astr_map[y][x] == '#':
                asteroids.append(Asteroid(astr_map, (x, y)))

    seeable = []
    for asteroid in asteroids:
        asteroid.analyze()
        seeable.append(asteroid.visible_asteroids())

    print(max(seeable))


def part02():
    asteroids = []
    astr_map = get_input()
    for y in range(len(astr_map)):
        for x in range(len(astr_map[y])):
            if astr_map[y][x] == '#':
                asteroids.append(Asteroid(astr_map, (x, y)))

    seeable = []
    for asteroid in asteroids:
        asteroid.analyze()
        seeable.append(asteroid.visible_asteroids())
    # Select asteroid which sees more asteroids than the others
    the_one = asteroids[seeable.index(max(seeable))]
    the_one.vaporize()


part01()
part02()