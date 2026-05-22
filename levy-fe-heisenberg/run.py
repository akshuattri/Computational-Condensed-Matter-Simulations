import numpy as np
from tqdm import tqdm

from src.structure import read_poscar
from src.supercell import build_supercell
from src.neighbors import build_neighbor_list
from src.spins import initialize_spins
from src.montecarlo import monte_carlo_step
from src.observables import (
    magnetization,
    total_energy
)
from src.plotting import plot_quantity

# ==========================================
# Read input
# ==========================================

params = {}

with open('input.dat') as f:

    for line in f:

        line = line.strip()

        if not line:
            continue

        if line.startswith('#'):
            continue

        key, value = line.split('=')

        params[key.strip()] = value.strip()

# ==========================================

SUPERCELL = int(params['SUPERCELL'])

J = float(params['J_EXCHANGE'])

MC_EQ = int(params['MC_EQUILIBRATION'])

MC_MEAS = int(params['MC_MEASUREMENTS'])

TEMP_START = float(params['TEMP_START'])

TEMP_END = float(params['TEMP_END'])

TEMP_POINTS = int(params['TEMP_POINTS'])

CUTOFF = float(params['CUTOFF_RADIUS'])

ALPHA = float(params['LEVY_ALPHA'])

np.random.seed(
    int(params['RANDOM_SEED'])
)

# ==========================================

lattice, positions = read_poscar(
    'POSCAR'
)

positions = build_supercell(
    lattice,
    positions,
    SUPERCELL
)

neighbors = build_neighbor_list(
    positions,
    CUTOFF
)

N = len(positions)

temperatures = np.linspace(
    TEMP_START,
    TEMP_END,
    TEMP_POINTS
)

magnetizations = []

heat_capacities = []

susceptibilities = []

# ==========================================

for T in tqdm(temperatures):

    spins = initialize_spins(N)

    # Equilibration

    for _ in range(MC_EQ):

        monte_carlo_step(
            spins,
            neighbors,
            J,
            T,
            ALPHA
        )

    E_samples = []

    M_samples = []

    # Measurements

    for _ in range(MC_MEAS):

        monte_carlo_step(
            spins,
            neighbors,
            J,
            T,
            ALPHA
        )

        E = total_energy(
            spins,
            neighbors,
            J
        )

        M = magnetization(spins)

        E_samples.append(E)

        M_samples.append(M)

    E_samples = np.array(E_samples)

    M_samples = np.array(M_samples)

    E_avg = np.mean(E_samples)

    M_avg = np.mean(M_samples)

    Cv = (
        np.mean(E_samples**2)
        - E_avg**2
    ) / (T**2)

    Chi = (
        np.mean(M_samples**2)
        - M_avg**2
    ) / T

    magnetizations.append(M_avg / N)

    heat_capacities.append(Cv / N)

    susceptibilities.append(Chi / N)

# ==========================================

plot_quantity(
    temperatures,
    magnetizations,
    'Temperature (K)',
    'Magnetization',
    'figures/magnetization.png'
)

plot_quantity(
    temperatures,
    heat_capacities,
    'Temperature (K)',
    'Heat Capacity',
    'figures/heat_capacity.png'
)

plot_quantity(
    temperatures,
    susceptibilities,
    'Temperature (K)',
    'Susceptibility',
    'figures/susceptibility.png'
)

Tc_index = np.argmax(susceptibilities)

Tc = temperatures[Tc_index]

print(f'Estimated Curie Temperature: {Tc:.2f} K')
