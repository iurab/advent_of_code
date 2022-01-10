import math

with open('input') as file:
    lines = file.readlines()

def get_row(characters):
    row_min, row_max = 0, 127
    for char in characters:
        if char == 'F':
            row_max -= math.ceil((row_max - row_min) / 2)
        else:
            row_min += math.ceil((row_max - row_min) / 2)
    return row_min

def get_column(characters):
    column_min, column_max = 0, 7
    for char in characters:
        if char == 'L':
            column_max -= math.ceil((column_max - column_min) / 2)
        else:
            column_min += math.ceil((column_max - column_min) / 2)
    return column_min

# Part 01
seats = [get_row(line[:7]) * 8 + get_column(line[7:]) for line in lines]
print(max(seats))

# Part 02
seats.sort()
for index, seat in enumerate(seats):
    if seats[index+1] == seat + 2:
        print(seat+1)
        break