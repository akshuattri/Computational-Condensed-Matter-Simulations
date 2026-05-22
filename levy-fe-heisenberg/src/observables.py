import numpy as np

def magnetization(spins):

    M = np.sum(spins, axis=0)

    return np.linalg.norm(M)

def total_energy(spins, neighbors, J):

    E = 0

    N = len(spins)

    for i in range(N):

        for j in neighbors[i]:

            E += -J * np.dot(
                spins[i],
                spins[j]
            )

    return E / 2
