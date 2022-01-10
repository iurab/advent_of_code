import numpy

def get_input():
    with open("input") as file:
        # Get drawn numbers
        numbers = list(map(int, file.readline().split(",")))
        # Get boards
        boards, board = [], []
        lines = file.readlines()
        for line in lines:
            if line.strip() == "":
                if board:
                    boards.append(board)
                board = []
                continue
            board.append(list(map(int, line.strip().split())))
        boards.append(board)
    return numbers, boards


def gen_mboards(number):
    mboards = []
    for _ in range(number):
        mboards.append(numpy.zeros((5,5),int))
    return mboards


def mark_number(boards, mboards, number):
    for k, board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == number:
                    mboards[k][i][j] = 1


def find_bingo(mboards, ignore):
    ok_boards = []
    for i, mboard in enumerate(mboards):
        if i in ignore:
            continue
        if bingo(mboard):
            ok_boards.append(i)
    return ok_boards


def bingo(mboard):
    # Check row
    for row in mboard:
        res = all(dot == 1 for dot in row)
        if res:
            return True
    # Check columns
    for j in range(len(mboard[0])):
        column = [row[j] for row in mboard]
        res = all(dot == 1 for dot in column)
        if res:
            return True
    return False

def sum_unmarked(board, mboard):
    usum = 0
    for i in range(5):
        for j in range(5):
            usum += board[i][j] if mboard[i][j] == 0 else 0
    return usum


def part01(numbers, boards):
    mboards = gen_mboards(len(boards))
    for number in numbers:
        mark_number(boards, mboards, number)
        winner = find_bingo(mboards, [])
        if winner:
            break
    usum = sum_unmarked(boards[winner], mboards[winner])
    print(usum * number)

def part02(numbers, boards):
    winners = []
    mboards = gen_mboards(len(boards))
    for number in numbers:
        mark_number(boards, mboards, number)
        ok_boards = find_bingo(mboards, winners)
        if ok_boards != []:
            winners.extend(ok_boards)
            usum = sum_unmarked(boards[winners[-1]], mboards[winners[-1]])
            print(usum * number)


if __name__ == "__main__":
    numbers, boards = get_input()
    # part01(numbers, boards)
    part02(numbers, boards)
