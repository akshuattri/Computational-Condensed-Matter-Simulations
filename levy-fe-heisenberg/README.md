# Levy-Fe-Heisenberg

Exploratory simulations of magnetic spin systems using the classical Heisenberg model and Levy-type magnetic interactions.

This project was developed for learning, numerical experimentation, and research training in computational condensed matter physics and magnetic many-body systems.

---

# Physics

The magnetic interactions are modeled using the classical Heisenberg Hamiltonian:

$$
H = -\sum_{ij} J_{ij}\,\vec{S}_i \cdot \vec{S}_j
$$

where:

- $J_{ij}$ = exchange interaction strength
- $\vec{S}_i$, $\vec{S}_j$ = neighboring spin vectors

The probability of accepting a Monte Carlo spin update follows the Metropolis criterion:

$$
P = \exp\left(-\frac{\Delta E}{k_B T}\right)
$$

where:

- $\Delta E$ = energy difference
- $k_B$ = Boltzmann constant
- $T$ = temperature

The simulations investigate magnetic ordering, thermal fluctuations, and spin dynamics in ferromagnetic systems.

---

# Features

- Classical Heisenberg spin simulations
- Monte Carlo sampling
- Magnetization analysis
- Thermal fluctuation studies
- Spin interaction modeling
- Magnetic phase behavior

---

# Repository Structure

```text
levy-fe-heisenberg/

├── POSCAR
├── input.dat
├── run.py
├── requirements.txt
├── README.md
├── src/
├── data/
└── venv/
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

- Magnetization evolution
- Energy fluctuations
- Spin configurations
- Thermal observables
- Statistical averages

Generated data and plots are stored in the project directories.

---

# Learning Objectives

This project was developed to explore:

- Heisenberg spin systems
- Monte Carlo techniques
- Ferromagnetism
- Statistical mechanics
- Thermal magnetic behavior
- Computational condensed matter physics

---

# References

- Classical Heisenberg model
- Monte Carlo methods in statistical physics
- Magnetic many-body systems
- Computational condensed matter simulations

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
