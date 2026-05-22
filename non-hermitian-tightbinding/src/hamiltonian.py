import numpy as np

def build_hamiltonian(L, t1, t2, gamma, boundary='OBC'):

    size = 2 * L

    H = np.zeros((size, size), dtype=complex)

    for n in range(L):

        a = 2 * n
        b = 2 * n + 1

        # intracell hopping
        H[a, b] = t1 + gamma
        H[b, a] = t1 - gamma

        # intercell hopping
        if n < L - 1:

            next_a = 2 * (n + 1)

            H[b, next_a] = t2
            H[next_a, b] = t2

    # periodic boundary
    if boundary == 'PBC':

        H[2*L - 1, 0] = t2
        H[0, 2*L - 1] = t2

    return H
