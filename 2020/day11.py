with open('input') as file:
    layout = [list(line.strip()) for line in file.readlines()]


def neighbours_1(pos_x, pos_y, layout):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if 0 <= pos_x + i < len(layout) and 0 <= pos_y + j < len(layout[0]):
                neighbours += 1 if layout[pos_x + i][pos_y + j] == '#' else 0
    return neighbours


def neighbours_2(pos_x, pos_y, layout):
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            seight_x = pos_x
            seight_y = pos_y
            while 0 <= seight_x + i < len(layout) and 0 <= seight_y + j < len(layout[0]):
                seight_x += i
                seight_y += j
                neighbours += 1 if layout[seight_x][seight_y] == '#' else 0
                if layout[seight_x][seight_y] in ['#', 'L']:
                    break
    return neighbours


def apply_rules(layout, part):
    new_layout = []
    for i, row in enumerate(layout):
        new_row = []
        for j, position in enumerate(row):
            # Part 01
            if part == 1:
                if position == 'L' and neighbours_1(i, j, layout) == 0:
                    new_row.append('#')
                elif position == '#' and neighbours_1(i, j, layout) >= 4:
                    new_row.append('L')
                else:
                    new_row.append(position)
            # Part 02
            elif part == 2:
                if position == 'L' and neighbours_2(i, j, layout) == 0:
                    new_row.append('#')
                elif position == '#' and neighbours_2(i, j, layout) >= 5:
                    new_row.append('L')
                else:
                    new_row.append(position)
        new_layout.append(new_row)
    return layout != new_layout, new_layout


# Part 01
layout_1 = layout[:]
while True:
    changes, layout_1 = apply_rules(layout_1, 1)
    if not changes:
        break

print(sum([row.count('#') for row in layout_1]))

# Part 02
layout_2 = layout[:]
while True:
    changes, layout_2 = apply_rules(layout_2, 2)
    if not changes:
        break

print(sum([row.count('#') for row in layout_2]))
