import numpy as np

def green_function(
    E,
    H,
    eta,
    SigmaL,
    SigmaR
):

    N = H.shape[0]

    I = np.eye(N)

    G = np.linalg.inv(
        (E + 1j*eta)*I
        - H
        - SigmaL
        - SigmaR
    )

    return G
