import numpy as np

def diagonalize(H):

    eigenvalues, eigenvectors = np.linalg.eig(H)

    return eigenvalues, eigenvectors
