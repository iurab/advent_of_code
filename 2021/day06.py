from collections import defaultdict

def get_input():
    with open('input') as file:
        lfishes = list(map(int,file.readline().strip().split(',')))
    print(lfishes)
    return lfishes

def part01(lfishes):
    for _ in range(80):
        n_lfishes = len(lfishes)
        for i in range(n_lfishes):
            if lfishes[i] == 0:
                lfishes[i] = 6
                lfishes.append(8)
            else:
                lfishes[i] -= 1
    print(len(lfishes))


def part02(lfishes):
    d_lfishes = defaultdict(int)
    for lfish in lfishes:
        d_lfishes[lfish] += 1
    tmp_dict = defaultdict(int)
    for _ in range(256):
        tmp_dict = d_lfishes.copy()
        for i in range(1,9):
            d_lfishes[i-1] = d_lfishes[i]
        d_lfishes[8] = tmp_dict[0]
        d_lfishes[6] += tmp_dict[0]
    print(sum(d_lfishes.values()))
    


if __name__ == '__main__':
    lfishes = get_input()
    part01(lfishes[:])
    part02(lfishes[:])