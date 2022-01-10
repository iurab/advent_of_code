puzz_in = 793031


def part01():
    # Initialize values
    elf_1 = 0
    elf_2 = 1
    scores = [3, 7]
    # Create the necessary recipes
    while len(scores) < puzz_in + 10:
        total = scores[elf_1] + scores[elf_2]
        scores.extend(divmod(total, 10) if total >= 10 else (total, ))
        elf_1 = (elf_1 + 1 + scores[elf_1]) % len(scores)
        elf_2 = (elf_2 + 1 + scores[elf_2]) % len(scores)

    last_10 = scores[-10:]
    print(''.join(str(score) for score in last_10))


def part02():
    # Initialize values
    elf_1 = 0
    elf_2 = 1
    scores = [3, 7]
    digits = [int(digit) for digit in str(puzz_in)]
    # Create the necessary recipes
    # Look for to -6: or -7:-1 because it can be the case that 2 recipes can be added
    while scores[-len(digits):] != digits and scores[-len(digits) -
                                                     1:-1] != digits:
        total = scores[elf_1] + scores[elf_2]
        scores.extend(divmod(total, 10) if total >= 10 else (total, ))
        elf_1 = (elf_1 + 1 + scores[elf_1]) % len(scores)
        elf_2 = (elf_2 + 1 + scores[elf_2]) % len(scores)
    print(
        len(scores) - len(digits) -
        (0 if scores[-len(digits):] == digits else 1))


# part01()
part02()
