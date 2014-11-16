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




neat = tm.TuringMachine(12,
  [
    [False, False,  4, False, True,   2, True,  False,  9],
    [True,  False, 12, False, False,  0, True,  True,   7],
    [True,  False,  6, False, False, 12, False, False,  1],
    [True,  True,   7, True,  False, 11, False, False,  6],
    [False, True,  11, False, False,  5, False, True,   5],
    [False, True,   4, False, False, 12, True,  True,  10],
    [False, True,   8, True,  True,   3, True,  True,  11],
    [False, False,  7, True,  False, 12, True,  False, 10],
    [True,  False,  9, True,  True,   5, False, False, 11],
    [False, False,  3, True,  True,   2, True,  False,  6],
    [True,  False, 10, True,  False, 11, False, True,  11],
    [True,  False,  3, True,  False,  8, True,  False,  2]
  ],
  random.randint(0, 2**32))
