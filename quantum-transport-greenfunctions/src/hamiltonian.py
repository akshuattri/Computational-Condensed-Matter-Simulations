import numpy as np

def build_hamiltonian(
    N,
    epsilon,
    t
):

    H = np.zeros((N,N), dtype=complex)

    for i in range(N):

        H[i,i] = epsilon

    for i in range(N-1):

        H[i,i+1] = -t

        H[i+1,i] = -t

    return H
