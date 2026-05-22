import numpy as np

def initialize_spins(N):

    spins = np.random.normal(size=(N,3))

    norms = np.linalg.norm(spins, axis=1)

    spins /= norms[:,None]

    return spins
