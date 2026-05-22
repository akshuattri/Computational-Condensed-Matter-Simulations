import numpy as np
from tqdm import tqdm

from src.hamiltonian import build_hamiltonian

from src.greens import green_function

from src.transport import (
    self_energy,
    gamma_matrix,
    transmission
)

from src.observables import density_of_states

from src.plotting import plot_data

# ====================================

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

# ====================================

N = int(params['SYSTEM_SIZE'])

epsilon = float(params['ONSITE_ENERGY'])

t = float(params['HOPPING'])

eta = float(params['ETA'])

Emin = float(params['ENERGY_MIN'])

Emax = float(params['ENERGY_MAX'])

Epoints = int(params['ENERGY_POINTS'])

# ====================================

H = build_hamiltonian(
    N,
    epsilon,
    t
)

SigmaL = self_energy(
    N,
    gamma=1.0,
    side='left'
)

SigmaR = self_energy(
    N,
    gamma=1.0,
    side='right'
)

GammaL = gamma_matrix(SigmaL)

GammaR = gamma_matrix(SigmaR)

energies = np.linspace(
    Emin,
    Emax,
    Epoints
)

dos_values = []

transmission_values = []

# ====================================

for E in tqdm(energies):

    G = green_function(
        E,
        H,
        eta,
        SigmaL,
        SigmaR
    )

    dos = density_of_states(G)

    T = transmission(
        G,
        GammaL,
        GammaR
    )

    dos_values.append(dos)

    transmission_values.append(T)

# ====================================

plot_data(
    energies,
    dos_values,
    'Energy',
    'DOS',
    'figures/dos.png'
)

plot_data(
    energies,
    transmission_values,
    'Energy',
    'Transmission',
    'figures/transmission.png'
)

print('Transport simulation complete.')
