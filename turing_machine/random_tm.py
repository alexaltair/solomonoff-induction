import turing_machine as tm
import random

def rand_bool():
    return random.choice([False, True])

def rand_state(n):
    return [rand_bool(), rand_bool(), random.randint(0, n),
            rand_bool(), rand_bool(), random.randint(0, n),
            rand_bool(), rand_bool(), random.randint(0, n)]

def rand_tm(number_of_states, tape_length):
    return tm.TuringMachine(
        number_of_states,
        [rand_state(number_of_states) for i in range(number_of_states)],
        random.randint(0, 2**tape_length))
