def spinlock_alg_1(steps):
    state = [0]
    position = 0
    for new_value in range(1, 2018):
        position = (position + steps + 1) % len(state)
        state.insert(position + 1, new_value)
    print(state[state.index(2017) + 1])
    # print(state)


def spinlock_alg_2(steps):
    position = 0
    state_size = 1
    for new_value in range(1, 50000001):
        position = (position + steps + 1) % state_size
        if position == 0:
            print(new_value)
        state_size += 1


def main():
    spinlock_alg_1(337)
    spinlock_alg_2(337)


if __name__ == '__main__':
    main()