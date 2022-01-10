def load_input(filename):
    with open(filename, "rt") as f:
        lines = f.readlines()
    state = "...." + lines[0].split()[2] + "...."
    rules = {l[:5] for l in lines[2:] if l.rstrip()[-1] == "#"}
    return rules, state, 4

def evolve(filename, gens):
    rules, state, center_idx = load_input(filename)
    for _ in range(1,gens+1):
        new_state = ["."] * len(state)
        for idx in range(2, len(state) - 2):
            if state[(idx-2):(idx+3)] in rules:
                new_state[idx] = "#"
        state = "".join(new_state)
        if state[0:4] != "....":
            state = "...." + state
            center_idx += 4
        if state[-4:] != "....":
            state = state + "...."
    return sum(i-center_idx for i, c in enumerate(state) if c == "#")

print("task1:", evolve("input", gens=20))
# task2: 50000000000 generations is way too many, even for a non-bruteforce solution
# i.e. there has to be some closed-form constant time solution. by observing the counts
# for some generations one can see that after generation 117 the counts always change by +55.
# 117 and 55 are probably only valid for my specific input though.
print("task2:", evolve("input", gens=98) + 25*(50000000000-98))
# for i in range(90, 150):
#     print(i, evolve('intput', gens=i))
#     input('')