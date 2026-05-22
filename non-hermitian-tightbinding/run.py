import numpy as np

from src.input_reader import read_input
from src.hamiltonian import build_hamiltonian
from src.diagonalization import diagonalize
from src.observables import probability_density
from src.plotting import (
    plot_complex_spectrum,
    plot_edge_state
)

# Read input

params = read_input('input.dat')

L = int(params['LATTICE_SIZE'])

t1 = float(params['T1'])
t2 = float(params['T2'])

gamma = float(params['GAMMA'])

boundary = params['BOUNDARY']

save_eigenvectors = params['SAVE_EIGENVECTORS']

# Build Hamiltonian

H = build_hamiltonian(
    L,
    t1,
    t2,
    gamma,
    boundary
)

# Diagonalization

eigenvalues, eigenvectors = diagonalize(H)

# Save eigenvalues

np.savetxt(
    'data/eigenvalues.dat',
    np.column_stack((
        eigenvalues.real,
        eigenvalues.imag
    ))
)

# Plot complex spectrum

plot_complex_spectrum(
    eigenvalues,
    'figures/complex_spectrum.png'
)

# Edge state analysis

idx = np.argmin(np.abs(eigenvalues))

edge_state = eigenvectors[:, idx]

prob = probability_density(edge_state)

np.savetxt(
    'data/edge_state_probability.dat',
    prob
)

plot_edge_state(
    prob,
    'figures/edge_state.png'
)

print('Simulation complete.')
