import turing_machine as tm
import random

does_nothing = tm.TuringMachine(1, [[False, True, 0, False, True, 1, True,  True, 1]], random.randint(0, 2**16))
inverter     = tm.TuringMachine(1, [[False, True, 0, True,  True, 1, False, True, 1]], random.randint(0, 2**16))
false_tm     = tm.TuringMachine(1, [[False, True, 0, False, True, 1, False, True, 1]], random.randint(0, 2**16))
true_tm      = tm.TuringMachine(1, [[True,  True, 0, True,  True, 1, True,  True, 1]], random.randint(0, 2**16))
