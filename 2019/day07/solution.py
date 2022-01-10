from itertools import permutations, cycle


def get_input():
    with open('input') as file:
        line = file.readline().split(',')
    data = list(map(int, line))
    return data


class Amp:
    def __init__(self, opcodes, phase):
        self.opcodes = opcodes
        self.phase = phase
        self.inputs = []
        self.outputs = []
        self.inputs.append(phase)
        self.index = 0
        self.halt = False
        self.instructions = {
            1: self.f_add,
            2: self.f_mul,
            3: self.f_in,
            4: self.f_out,
            5: self.f_jump_true,
            6: self.f_jump_false,
            7: self.f_less_than,
            8: self.f_equal
        }

    def f_add(self, parameters):
        self.opcodes[parameters[2]] = self.opcodes[
            parameters[0]] + self.opcodes[parameters[1]]
        self.index += 1 + len(parameters)

    def f_mul(self, parameters):
        self.opcodes[parameters[2]] = self.opcodes[
            parameters[0]] * self.opcodes[parameters[1]]
        self.index += 1 + len(parameters)

    def f_in(self, parameters):
        self.opcodes[parameters[0]] = self.inputs.pop(0)
        self.index += 1 + len(parameters)

    def f_out(self, parameters):
        self.outputs.append(self.opcodes[parameters[0]])
        self.index += 1 + len(parameters)

    def f_jump_true(self, parameters):
        if self.opcodes[parameters[0]] != 0:
            self.index = self.opcodes[parameters[1]]
        else:
            self.index += 1 + len(parameters)

    def f_jump_false(self, parameters):
        if self.opcodes[parameters[0]] == 0:
            self.index = self.opcodes[parameters[1]]
        else:
            self.index += 1 + len(parameters)

    def f_less_than(self, parameters):
        self.opcodes[parameters[2]] = 1 if self.opcodes[
            parameters[0]] < self.opcodes[parameters[1]] else 0
        self.index += 1 + len(parameters)

    def f_equal(self, parameters):
        self.opcodes[parameters[2]] = 1 if self.opcodes[
            parameters[0]] == self.opcodes[parameters[1]] else 0
        self.index += 1 + len(parameters)

    def get_parameters(self):
        # Get command
        command = self.opcodes[self.index] % 100
        # Get mode of parameters
        if command in [3, 4]:
            nr_param = 1
        elif command in [5, 6]:
            nr_param = 2
        elif command in [1, 2, 7, 8]:
            nr_param = 3
        modes = []
        for i in range(2, 2 + nr_param):
            modes.append(self.opcodes[self.index] // 10**i % 10)
        # Get parameters position in opcode
        parameters = []
        for i in range(len(modes)):
            if modes[i] == 0:
                # Position mode
                parameters.append(self.opcodes[self.index + 1 + i])
            else:
                # Immediate mode
                parameters.append(self.index + 1 + i)
        return parameters

    def compute(self, value) -> int:
        self.inputs.append(value)
        while self.opcodes[self.index] != 99:
            # Get command
            command = self.opcodes[self.index] % 100
            # Get mode of parameters
            parameters = self.get_parameters()
            # Execute command
            instruction = self.instructions[command]
            instruction(parameters)
            if len(self.outputs) > 0:
                return self.outputs.pop(0)
        self.halt = True
        return None


def part01():
    opcodes = get_input()
    max_thrust = 0
    # Generate combinations of phases - from 0 to 4
    for phases in list(permutations(range(5))):
        in_sig = 0
        for phase in phases:
            amp = Amp(opcodes, phase)
            out_sig = amp.compute(in_sig)
            in_sig = out_sig
        max_thrust = max(max_thrust, out_sig)
    print(max_thrust)


def part02():
    opcodes = get_input()
    max_thrust = 0
    # Generate combinations of phases - from 5 to 9
    for phases in list(permutations(range(5, 10))):
        # Generate Amps with the current phases
        amps = []
        for phase in phases:
            amps.append(Amp(opcodes[:], phase))
        in_sig = 0
        outputs = [0]
        for amp in cycle(amps):
            if not amp.halt:
                out_sig = amp.compute(in_sig)
            if out_sig:
                outputs.append(out_sig)
                in_sig = out_sig
            else:
                break
        max_thrust = max(max_thrust, outputs[-1])
    print(max_thrust)


if __name__ == '__main__':
    part01()
    part02()