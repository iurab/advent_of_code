class IntCode:
    def __init__(self, opcodes, func = None):
        self.mem = opcodes.copy()

        self.done = False

        self.inputs = []

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
            9: self.f_update_addr,
            99: self.f_terminate
        }

        self.find_input = func

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
        self.mem[parameters[0]] = self.get_input()
        self.move_index(parameters)

    def f_out(self, parameters):
        self.output = self.mem[parameters[0]]
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

    def f_terminate(self, parameters):
        self.done = True

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
        else:
            nr_param = 0
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

    def get_input(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        else:
            return self.find_input()

    def set_input(self, value):
        self.inputs.append(value)


    def set_address(self, address, value):
        self.mem[address] = value

    def run(self):
        self.output = None
        while not self.done and self.output is None:
            # Get command
            command = self.mem[self.index] % 100
            # Get mode of parameters
            parameters = self.get_parameters()
            # Execute command
            instruction = self.instructions[command]
            instruction(parameters)
        return self.output