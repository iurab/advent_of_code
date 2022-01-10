with open('input') as file:
    instructions = [[line[0], int(line[1:])] for line in file.readlines()]

# Part 01
class Ferry_01:

    N = E = 0
    facing = 'E'

    def __init__(self):
        pass

    def navigate(self, instructions):
        for instruction in instructions:
            action, value = instruction
            if action in 'NWSEF':
                self.move(action, value)
            else:
                self.rotate(action, value)
        print(abs(self.N) + abs(self.E))

    def move(self, action, value):
        direction = self.facing if action == 'F' else action
        if direction in 'NS':
            self.N += value if direction == 'N' else -value
        else:
            self.E += value if direction == 'E' else -value

    def rotate(self, action, value):
        compass = list('NESW')
        rotation = value // 90 if action == 'R' else -value // 90
        self.facing = compass[(compass.index(self.facing) + rotation) % 4]

ferry = Ferry_01()
ferry.navigate(instructions)

class Ferry_02:

    N = E = 0
    waypoint = {'E': 10, 'N': 1}

    def __init__(self):
        pass

    def navigate(self, instructions):
        for instruction in instructions:
            action, value = instruction
            if action in 'NWSE':
                self.move(action, value)
            elif action in 'LR':
                self.rotate(action, value)
            else:
                self.travel(action, value)
        print(abs(self.N) + abs(self.E))

    def move(self, direction, value):
        if direction in 'EW':
            self.waypoint['E'] += value if direction == 'E' else -value
        else:
            self.waypoint['N'] += value if direction == 'N' else -value

    def rotate(self, direction, value):
        rotation = value // 90 if direction == 'R' else -value // 90
        new_waypoint = {}
        if rotation in [1,-3]:
            new_waypoint['E'] = self.waypoint['N']
            new_waypoint['N'] = -self.waypoint['E']
        elif rotation in [2, -2]:
            new_waypoint['E'] = -self.waypoint['E']
            new_waypoint['N'] = -self.waypoint['N']
        elif rotation in [3, -1]:
            new_waypoint['E'] = -self.waypoint['N']
            new_waypoint['N'] = self.waypoint['E']
        if rotation in [-3, -2, -1, 1, 2, 3]:
            self.waypoint = new_waypoint

    def travel(self, direction, value):
        self.N += value * self.waypoint['N']
        self.E += value * self.waypoint['E']


ferry = Ferry_02()
ferry.navigate(instructions)
