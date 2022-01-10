def get_input():
    # Get data
    with open('input') as file:
        data = file.read().splitlines()
    # Adapt / convert information
    masses = list(map(int, data))
    return masses


def calc_fuel(mass):
    fuel = mass // 3 - 2
    return fuel if fuel > 0 else 0


def sum_fuel_of_fuel(mass, total=0):
    fuel = calc_fuel(mass)
    if fuel == 0:
        return total
    else:
        return sum_fuel_of_fuel(fuel, total + fuel)


def part01(masses):
    # Fuel requirement
    fuel = 0
    for mass in masses:
        fuel += calc_fuel(mass)
    print(fuel)


def part02(masses):
    # Fuel requirement
    fuel = 0
    for mass in masses:
        fuel += sum_fuel_of_fuel(mass)
    print(fuel)


if __name__ == '__main__':
    info = get_input()
    part01(info)
    part02(info)