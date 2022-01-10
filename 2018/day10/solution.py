from parse import parse


def get_input():
    pos = []
    vel = []
    matcher = "position=<{pos_x:d}, {pos_y:d}> velocity=<{vel_x:d}, {vel_y:d}>"
    with open("input") as file:
        text = file.readlines()
    for line in text:
        r = parse(matcher, line)
        pos.append([r["pos_x"], r["pos_y"]])
        vel.append([r["vel_x"], r["vel_y"]])
    return pos, vel


def part01(sky):
    pos, vel = sky
    seconds = 0
    while True:
        for i in range(len(pos)):
            pos[i][0] += vel[i][0]
            pos[i][1] += vel[i][1]
        seconds += 1
        # Check if height is 10
        min_y = min([pos[i][1] for i in range(len(pos))])
        max_y = max([pos[i][1] for i in range(len(pos))])
        if max_y - min_y <= 10:
            print_points(sky)
            print(seconds)
            break


def print_points(sky):
    pos, _ = sky
    min_x = min([pos[i][0] for i in range(len(pos))])
    min_y = min([pos[i][1] for i in range(len(pos))])
    width = max([pos[i][0] for i in range(len(pos))]) - min_x + 1
    height = max([pos[i][1] for i in range(len(pos))]) - min_y + 1
    canvas = [['.'] * width for _ in range(height)]
    for i in range(len(pos)):
        canvas[pos[i][1] - min_y][pos[i][0] - min_x] = '#'
    for line in canvas:
        print(''.join(line))


if __name__ == "__main__":
    sky = get_input()
    part01(sky)
