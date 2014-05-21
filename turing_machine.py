class State():
    def __init__(self, ??):
        self.end_of_tape = ??
        self.write_false = ??
        self.move_false = ??
        self.write_true = ??
        self.move_true = ??

class TuringMachine():
    def __init__(self, n):
        # ?? Magic that translates int n into a starting tape and a collection of states.
        self.init_tape(??)
        self.init_states(??)

    def init_tape(self, ??):
        self.tape = [None]
        self.head = 0
        # turn ?? into tape contents

    def init_states(self, ??):
        self.state = 0
        self.states = State(??)

    def current_input(self):
        return self.tape[self.head]

    def is_end_of_tape(self):
        return self.current_input == None

    def write(self, boolean):
        # Check that this isn't the end of the tape, and that we are passed a proper bool.
        self.tape[self.head] = boolean

    def move(self, direction):
        if direction == None:
            pass
        elif direction == False:
            self.head -= 1
        elif direction == True:
            self.head += 1
        else:
            raise Exception
        # If head is out of bounds, raise Exception

    def state(self, state_index):
        params = self.states[state_index]
        if self.current_input() == None:
            # Can't overwrite the end of the tape.
            self.move(params.end_of_tape)
        elif self.current_input() == False:
            self.write(params.write_false)
            self.move(params.move_false)
        elif self.current_input() == True:
            self.write(params.write_true)
            self.move(params.move_true)
        else:
            raise Exception

        # ?? goto another state or halt
