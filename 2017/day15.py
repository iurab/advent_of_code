def generator(value, divisor, multiplied=1):
    while True:
        value = value * divisor % 2147483647
        if value % multiplied == 0:
            yield value


def judge_1():
    gen_a = generator(679, 16807)
    gen_b = generator(771, 48271)
    print(
        sum(
            next(gen_a) & 0xFFFF == next(gen_b) & 0xFFFF
            for _ in range(40000000)))


def judge_2():
    gen_a = generator(679, 16807, 4)
    gen_b = generator(771, 48271, 8)
    print(
        sum(
            next(gen_a) & 0xFFFF == next(gen_b) & 0xFFFF
            for _ in range(5000000)))


def main():
    judge_1()
    judge_2()


if __name__ == '__main__':
    main()
