# Fe Heisenberg Monte Carlo

Exploratory Monte Carlo simulations of ferromagnetic iron using the classical Heisenberg spin model.

This project was developed for learning, numerical experimentation, and research training in computational condensed matter physics and magnetic many-body systems.

---

# Physics

The classical Heisenberg Hamiltonian is given by:

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

The simulation studies thermal magnetic behavior and spin ordering in ferromagnetic systems.

---

# Features

- Classical Heisenberg spin simulations
- Monte Carlo sampling
- Metropolis algorithm
- Magnetization calculations
- Thermal fluctuation analysis
- Spin configuration evolution

---

# Repository Structure

```text
fe-herisenberg-montecarlo/

├── POSCAR
├── input.dat
├── run.py
├── requirements.txt
├── README.md
├── src/
├── data/
├── figures/
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

Run the Monte Carlo simulation:

```bash
python run.py
```

---

# Outputs

The simulation generates:

- Magnetization evolution
- Spin configurations
- Energy fluctuations
- Thermal averages
- Statistical observables

Generated plots are stored in:

```text
figures/
```

---

# Learning Objectives

This project was developed to explore:

- Heisenberg spin systems
- Monte Carlo methods
- Ferromagnetism
- Statistical mechanics
- Magnetic phase behavior
- Numerical simulation techniques

---

# References

- Classical Heisenberg model
- Monte Carlo methods in statistical physics
- Metropolis algorithm
- Computational condensed matter physics

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
