class IntCode:
    def __init__(self, opcodes):
        self.mem = opcodes.copy()

        self.inputs = []
        self.outputs = []

        self.index = 0
        self.addr = 0

        self.instructions = {
            1: self.f_add,
            2: self.f_mul,
            3: self.f_in,
            4: self.f_out,
            5: self.f_jump_true,
            6: self.f_jump_false,
            7: self.f_less_than,
            8: self.f_equal,
            9: self.f_update_addr
        }

    def move_index(self, parameters):
        self.index += 1 + len(parameters)

    def f_add(self, parameters):
        self.mem[
            parameters[2]] = self.mem[parameters[0]] + self.mem[parameters[1]]
        self.move_index(parameters)

    def f_mul(self, parameters):
        self.mem[
            parameters[2]] = self.mem[parameters[0]] * self.mem[parameters[1]]
        self.move_index(parameters)

    def f_in(self, parameters):
        self.mem[parameters[0]] = self.inputs.pop(0)
        self.move_index(parameters)

    def f_out(self, parameters):
        self.outputs.append(self.mem[parameters[0]])
        self.move_index(parameters)

    def f_jump_true(self, parameters):
        if self.mem[parameters[0]] != 0:
            self.index = self.mem[parameters[1]]
        else:
            self.move_index(parameters)

    def f_jump_false(self, parameters):
        if self.mem[parameters[0]] == 0:
            self.index = self.mem[parameters[1]]
        else:
            self.move_index(parameters)

    def f_less_than(self, parameters):
        self.mem[parameters[2]] = 1 if self.mem[parameters[0]] < self.mem[
            parameters[1]] else 0
        self.move_index(parameters)

    def f_equal(self, parameters):
        self.mem[parameters[2]] = 1 if self.mem[parameters[0]] == self.mem[
            parameters[1]] else 0
        self.move_index(parameters)

    def f_update_addr(self, parameters):
        self.addr += self.mem[parameters[0]]
        self.move_index(parameters)

    def get_parameters(self):
        # Get command
        command = self.mem[self.index] % 100
        # Get mode of parameters
        if command in [3, 4, 9]:
            nr_param = 1
        elif command in [5, 6]:
            nr_param = 2
        elif command in [1, 2, 7, 8]:
            nr_param = 3
        modes = []
        for i in range(2, 2 + nr_param):
            modes.append(self.mem[self.index] // 10**i % 10)
        # Get parameters position in opcode
        parameters = []
        for i in range(len(modes)):
            if modes[i] == 0:
                # Position mode
                parameters.append(self.mem[self.index + 1 + i])
            elif modes[i] == 1:
                # Immediate mode
                parameters.append(self.index + 1 + i)
            else:
                # Relative mode
                parameters.append(self.mem[self.index + 1 + i] + self.addr)
        return parameters

    def run(self, value=None):
        if value:
            self.inputs.append(value)
        while self.mem[self.index] != 99:
            # Get command
            command = self.mem[self.index] % 100
            # Get mode of parameters
            parameters = self.get_parameters()
            # Execute command
            instruction = self.instructions[command]
            instruction(parameters)
            if self.outputs:
                break


def get_input():
    with open('input') as file:
        line = file.readline().split(',')
    data = {pos: int(x) for pos, x in enumerate(line)}
    return data


def part01():
    opcodes = get_input()
    computer = IntCode(opcodes)
    computer.run(1)
    print(computer.outputs)

def part02():
    opcodes = get_input()
    computer = IntCode(opcodes)
    computer.run(2)
    print(computer.outputs)


if __name__ == '__main__':
    part01()
    part02()