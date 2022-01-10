from parse import parse
from collections import namedtuple


class Moon:
    def __init__(self, position):
        self.position = position[:]
        self.velocity = [0,0,0]

    def all_moons(self, all_moons):
        self.all_moons = all_moons

    def calc_gravity(self):
        for moon in self.all_moons:
            for i in range(len(self.position)):
                if self.position[i] < moon.position[i]:
                    self.velocity[i] += 1
                elif self.position[i] > moon.position[i]:
                    self.velocity[i] += -1

    def apply_velocity(self):
        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

    def total_energy(self):
        potential = sum(abs(value) for value in self.position)
        kinetic = sum(abs(value) for value in self.velocity)
        return potential * kinetic


def get_input():
    matcher = '<x={pos_x:d}, y={pos_y:d}, z={pos_z:d}>'
    with open('input') as file:
        text = file.readlines()
    moons = []
    for i, line in enumerate(text):
        r = parse(matcher, line)
        moons.append(Moon([r['pos_x'], r['pos_y'], r['pos_z']]))
    return moons


def part01():
    moons = get_input()
    for moon in moons:
        moon.all_moons(moons)
    for _ in range(1000):
        for moon in moons:
            moon.calc_gravity()
        for moon in moons:
            moon.apply_velocity()
    total = sum([moon.total_energy() for moon in moons])

    print(total)

def part02():
    moons = get_input()
    for moon in moons:
        moon.all_moons(moons)
    iterations = 0
    seen = set()
    while True:
        for moon in moons:
            moon.calc_gravity()
        for moon in moons:
            moon.apply_velocity()
        state = []
        for moon in moons:
            state.append(moon.position[2])
            state.append(moon.velocity[2])
        state = str(state)
        if state in seen:
            print(iterations)
            input()
        seen.add(state)
        iterations += 1





# part01()
part02()