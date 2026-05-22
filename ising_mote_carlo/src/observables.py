import numpy as np

def calculate_energy(spins, J):

    L = spins.shape[0]

    energy = 0

    for i in range(L):
        for j in range(L):

            S = spins[i, j]

            neighbors = (
                spins[(i + 1) % L, j] +
                spins[i, (j + 1) % L]
            )

            energy += -J * S * neighbors

    return energy / (L * L)

def calculate_magnetization(spins):

    return np.abs(np.sum(spins)) / spins.size
