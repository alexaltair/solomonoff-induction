class State():
    def __init__(self, params):
        # [bool, bool, int,
        #  bool, bool, int,
        #  bool, bool, int]
        (
            self.write_end,
            self.move_end,
            self.next_end,
            self.write_false,
            self.move_false,
            self.next_false,
            self.write_true,
            self.move_true,
            self.next_true
        ) = params

class TuringMachine():
    def __init__(self, number_of_states, state_array, tape_int):
        self._init_states(number_of_states, state_array)
        self._init_tape(tape_int)

    def _init_tape(self, tape_int):
        bin_string = bin(tape_int)[2:]
        self.tape = map(lambda digit: False if digit == '0' else True, bin_string)
        self.head = 0

    def _init_states(self, number_of_states, state_array):
        # Make sure 0<= state_array[i][3] <= number_of_states
        # Later, do cool state graph checking to make sure it's a connected graph
        #  & that at least one state points to halting state.
        self.states = map(State, state_array)
        self.states.insert(0, 'halt')
        self.state = 1

    def current_input(self):
        if self.head < len(self.tape):
            return self.tape[self.head]

    def write(self, boolean):
        # Check that this isn't the end of the tape, and that we are passed a proper bool.
        if self.current_input() == None:
            self.tape.append(boolean)
        else:
            self.tape[self.head] = boolean

    def move(self, direction):
        if direction == False:
            if self.head > 0:
                self.head -= 1
            # else it's at the start of the tape and we don't allow it to move off
        elif direction == True:
            self.head += 1
        else:
            raise Exception
        # If head is out of bounds, raise Exception

    def step(self):
        params = self.states[self.state]
        if params == 'halt':
            return 'halt'
        elif self.current_input() == None:
            self.write(params.write_end)
            self.move(params.move_end)
            self.state = params.next_end
        elif self.current_input() == False:
            self.write(params.write_false)
            self.move(params.move_false)
            self.state = params.next_false
        elif self.current_input() == True:
            self.write(params.write_true)
            self.move(params.move_true)
            self.state = params.next_true
        else:
            raise Exception

    def run(self):
        status = None
        while status == None:
            status = self.step()

    def __str__(self):
        tape = ''.join(map(lambda boolean: 'M' if boolean else '_', self.tape))
        return tape + " S:" + str(self.state) + " H:" + str(self.head)
