import numpy as np

with open('input') as file:
    seed = [list(line.strip()) for line in file.readlines()]
print(seed)

# create petri dish - 3d matrix
# Z X Y
petri_dish = np.zeros((13,13,20,20), dtype=int)
# place seed
for i, row in enumerate(seed):
    for j, cell in enumerate(row):
        petri_dish[6][6][i+6][j+6] = 1 if cell == '#' else 0
# game of life
for _ in range(6):
    petri_dish_next = petri_dish.copy()
    for w in range(petri_dish.shape[0]):
        for z in range(petri_dish.shape[1]):
            for x in range(petri_dish.shape[2]):
                for y in range(petri_dish.shape[3]):
                    # Slice bigger cube around cube - with all neighbours including it
                    w_slice = []
                    z_slice = []
                    x_slice = []
                    y_slice = []
                    for i in range(-1, 2):
                        if 0 <= w+i < petri_dish.shape[0]:
                            w_slice.append((w+i))
                        if 0 <= z+i < petri_dish.shape[1]:
                            z_slice.append((z+i))
                        if 0 <= x+i < petri_dish.shape[2]:
                            x_slice.append((x+i))
                        if 0 <= y+i < petri_dish.shape[3]:
                            y_slice.append((y+i))
                    ixgrd = np.ix_(w_slice, z_slice, x_slice, y_slice)
                    pocket_slice = petri_dish[ixgrd]
                    cube = petri_dish[w][z][x][y]
                    neighbours = np.sum(pocket_slice) - cube
                    if cube == 1:
                        petri_dish_next[w][z][x][y] = 1 if 2 <= neighbours <= 3 else 0
                    else:
                        petri_dish_next[w][z][x][y] = 1 if neighbours == 3 else 0
    petri_dish = petri_dish_next
print(np.sum(petri_dish))      
