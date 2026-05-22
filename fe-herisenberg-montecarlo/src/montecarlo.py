import numpy as np

def local_energy(i, spins, neighbors, J):

    E = 0

    Si = spins[i]

    for j in neighbors[i]:

        Sj = spins[j]

        E += -J * np.dot(Si, Sj)

    return E

def monte_carlo_step(spins, neighbors, J, T):

    N = len(spins)

    for _ in range(N):

        i = np.random.randint(0, N)

        old_spin = spins[i].copy()

        old_energy = local_energy(
            i,
            spins,
            neighbors,
            J
        )

        new_spin = np.random.normal(size=3)

        new_spin /= np.linalg.norm(new_spin)

        spins[i] = new_spin

        new_energy = local_energy(
            i,
            spins,
            neighbors,
            J
        )

        dE = new_energy - old_energy

        if dE > 0:

            if np.random.rand() > np.exp(-dE / T):

                spins[i] = old_spin
