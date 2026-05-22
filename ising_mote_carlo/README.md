# Ising Monte Carlo

Exploratory Monte Carlo simulations of the Ising model for learning statistical mechanics, phase transitions, and computational condensed matter physics.

---

# Physics

The Ising model describes interacting spins on a lattice.

The Hamiltonian is:

$$
H = -J \sum_{\langle i,j \rangle} S_i S_j
$$

where:

- $J$ = exchange interaction strength
- $S_i, S_j = \pm 1$ are spin variables
- $\langle i,j \rangle$ denotes nearest neighbors

The probability of accepting a spin flip in the Metropolis algorithm is:

$$
P = \exp\left(-\frac{\Delta E}{k_B T}\right)
$$

where:

- $\Delta E$ = energy difference
- $k_B$ = Boltzmann constant
- $T$ = temperature

The simulation studies thermal fluctuations and magnetic phase transitions.

---

# Features

- Monte Carlo spin updates
- Metropolis algorithm
- Magnetization calculations
- Energy analysis
- Thermal fluctuations
- Phase transition studies

---

# Repository Structure

```text
ising_mote_carlo/

├── input.dat
├── run.py
├── requirements.txt
├── README.md
├── src/
├── data/
└── figures/
```

---

# Requirements

- Python 3.x
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Simulation

Run the simulation:

```bash
python run.py
```

---

# Outputs

The simulation generates:

- Magnetization curves
- Energy evolution
- Spin configurations
- Temperature-dependent observables
- Statistical averages

Plots are stored in:

```text
figures/
```

---

# Learning Objectives

This project was developed to explore:

- Statistical mechanics
- Monte Carlo techniques
- Phase transitions
- Ferromagnetism
- Lattice spin systems
- Numerical simulation methods

---

# References

- Ising model
- Metropolis Monte Carlo algorithm
- Statistical mechanics
- Computational condensed matter physics

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
