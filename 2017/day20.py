from collections import defaultdict


class Particle:
    def __init__(self, position, velocity, acceleration, number):
        self.number = number
        # For fist part
        # self.position = [abs(x) for x in position]
        # self.velocity = [abs(x) for x in velocity]
        # self.acceleration = [abs(x) for x in acceleration]
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def step(self):
        for i in range(3):
            self.velocity[i] += self.acceleration[i]
            self.position[i] += self.velocity[i]


def gpu_calculation(puzzle_input):
    particles = {}
    for i, line in enumerate(puzzle_input):
        elements = line.strip().split(', ')
        position = [int(x) for x in elements[0].split('=')[1][1:-1].split(',')]
        velocity = [int(x) for x in elements[1].split('=')[1][1:-1].split(',')]
        acceleration = [
            int(x) for x in elements[2].split('=')[1][1:-1].split(',')
        ]
        particles[i] = Particle(position, velocity, acceleration, i)

    for _ in range(1000):
        # positions = [tuple(particle.position) for particle in particles]
        # seen = set()
        # duplicate = set()
        # # Search for positions which are the same
        # for position in positions:
        #     if position in seen:
        #         duplicate.add(position)
        #     else:
        #         seen.add(position)
        # # See if there are particles which collide
        # if len(duplicate) > 0:
        #     for particle in particles:
        #         if tuple(particle.position) in duplicate:
        #             particles.remove(particle)
        #     print(len(particles))
        # for particle in particles:
        #     particle.step()

        position_dict = defaultdict(list)
        for i, particle in particles.items():
            tuple_position = tuple(particle.position)
            position_dict[tuple_position].append(i)

        for tuple_position, list_index in position_dict.items():
            if len(list_index) > 1:
                for index in list_index:
                    particles.pop(index)
                print(len(particles))

        for _, particle in particles.items():
            particle.step()
    # particles.sort(
    #     key=
    #     lambda particle: (particle.acceleration, particle.velocity, particle.position)
    # )
    # print(particles[0].number)


def get_puzzle_input():
    with open('day20.txt', 'r') as file:
        puzzle_input = file.readlines()
    return puzzle_input


def main():
    puzzle_input = get_puzzle_input()
    gpu_calculation(puzzle_input)


if __name__ == '__main__':
    main()
