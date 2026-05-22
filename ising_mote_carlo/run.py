import numpy as np
from tqdm import tqdm

from src.input_reader import read_input
from src.lattice import initialize_lattice
from src.montecarlo import metropolis_step
from src.observables import (
    calculate_energy,
    calculate_magnetization
)
from src.plotting import plot_data

params = read_input('input.dat')

L = int(params['LATTICE_SIZE'])

J = float(params['J_COUPLING'])

MC_STEPS = int(params['MC_STEPS'])

TEMP_START = float(params['TEMP_START'])
TEMP_END = float(params['TEMP_END'])

TEMP_POINTS = int(params['TEMP_POINTS'])

SAVE_SPIN_CONFIG = params['SAVE_SPIN_CONFIG']

RANDOM_SEED = int(params['RANDOM_SEED'])

np.random.seed(RANDOM_SEED)

temperatures = np.linspace(
    TEMP_START,
    TEMP_END,
    TEMP_POINTS
)

magnetizations = []

energies = []


for T in tqdm(temperatures):

    spins = initialize_lattice(L)

    for step in range(MC_STEPS):

        metropolis_step(spins, T, J)

    M = calculate_magnetization(spins)

    E = calculate_energy(spins, J)

    magnetizations.append(M)

    energies.append(E)

np.savetxt(
    'data/magnetization.dat',
    np.column_stack((temperatures, magnetizations))
)

np.savetxt(
    'data/energy.dat',
    np.column_stack((temperatures, energies))
)

plot_data(
    temperatures,
    magnetizations,
    'Temperature',
    'Magnetization',
    'figures/magnetization.png'
)

plot_data(
    temperatures,
    energies,
    'Temperature',
    'Energy',
    'figures/energy.png'
)

print('Simulation complete.')
