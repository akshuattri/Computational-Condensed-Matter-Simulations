import numpy as np

def self_energy(
    N,
    gamma,
    side='left'
):

    Sigma = np.zeros((N,N), dtype=complex)

    if side == 'left':

        Sigma[0,0] = -1j*gamma

    elif side == 'right':

        Sigma[-1,-1] = -1j*gamma

    return Sigma

def gamma_matrix(Sigma):

    return 1j * (
        Sigma
        - Sigma.conjugate().T
    )

def transmission(
    G,
    GammaL,
    GammaR
):

    T = np.trace(
        GammaL
        @ G
        @ GammaR
        @ G.conjugate().T
    )

    return np.real(T)
