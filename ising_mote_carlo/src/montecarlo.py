import numpy as np

def metropolis_step(spins, T, J):

    L = spins.shape[0]

    for _ in range(L * L):

        i = np.random.randint(0, L)
        j = np.random.randint(0, L)

        s = spins[i, j]

        neighbors = (
            spins[(i + 1) % L, j] +
            spins[(i - 1) % L, j] +
            spins[i, (j + 1) % L] +
            spins[i, (j - 1) % L]
        )

        delta_E = 2 * J * s * neighbors

        if delta_E <= 0:

            s *= -1

        elif np.random.rand() < np.exp(-delta_E / T):

            s *= -1

        spins[i, j] = s
