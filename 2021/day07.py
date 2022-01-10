def get_input():
    with open("input") as file:
        positions = list(map(int, file.readline().split(",")))
    return positions


def part01(positions):
    fuel_consumptions = []
    for position in positions:
        fcons = sum(abs(position - x) for x in positions)
        fuel_consumptions.append(fcons)
    print(min(fuel_consumptions))


def part02(positions):
    fuel_consumptions = []
    for position in positions:
        fcons = sum(abs(position - x) * (abs(position - x) + 1) / 2 for x in positions)
        fuel_consumptions.append(fcons)
    print(min(fuel_consumptions))


if __name__ == "__main__":
    positions = get_input()
    part01(positions)
    part02(positions)
