import turing_machine as tm
import random

does_nothing  = tm.TuringMachine(1, [[False, True, 0, False, True, 1, True,  True, 1]], random.randint(0, 2**16))
inverter      = tm.TuringMachine(1, [[False, True, 0, True,  True, 1, False, True, 1]], random.randint(0, 2**16))
false_tm      = tm.TuringMachine(1, [[False, True, 0, False, True, 1, False, True, 1]], random.randint(0, 2**16))
true_tm       = tm.TuringMachine(1, [[True,  True, 0, True,  True, 1, True,  True, 1]], random.randint(0, 2**16))

# Broken because my TM specification doesn't allow writing before the beginning of the tape.
wolfram_smith = tm.TuringMachine(2, [[False,  True, 2, True,  False, 1, False,  False, 1],
                                     [True,  False, 1, True,  True, 2, None,  True, 1]],
                                     random.randint(0, 2**16))
# wolfram_smith.tape = [None]*16 + wolfram_smith.tape
# wolfram_smith.head = 20
