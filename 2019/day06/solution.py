from collections import Counter

def get_input():
    with open('input') as file:
        data = file.read().split()
    return data

def part01():
    data = get_input()
    orbits = {}
    for line in data:
        orbits[line[4:]] = line[0:3]
    nr_orbits = 0
    for obj in orbits:
        while orbits[obj] != 'COM':
            obj = orbits[obj]
            nr_orbits += 1
        nr_orbits += 1
    print(nr_orbits)

def part02():
    data = get_input()
    orbits = {}
    for line in data:
        orbits[line[4:]] = line[0:3]
    # Find path for YOU and SAN to COM
    paths = {'YOU': [], 'SAN': []}
    for obj in paths:
        origin = obj
        while orbits[obj] != 'COM':
            obj = orbits[obj]
            paths[origin].append(obj)
    # Find first common object
    for obj in paths['YOU']:
        if obj in paths['SAN']:
            common = obj
            break
    # Calculate distance
    print(paths['YOU'].index(common) + paths['SAN'].index(common))


if __name__ == '__main__':
    # part01()
    part02()