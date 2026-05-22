import numpy as np

def density_of_states(G):

    dos = -np.imag(
        np.trace(G)
    ) / np.pi

    return dos
