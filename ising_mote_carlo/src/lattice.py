import numpy as np

def initialize_lattice(L):

    spins = np.random.choice([-1, 1], size=(L, L))

    return spins
