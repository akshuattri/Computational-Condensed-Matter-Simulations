# Hysteresis Loop Simulation

Exploratory simulations of magnetic hysteresis behavior in ferromagnetic systems for learning and numerical experimentation in computational condensed matter physics.

---

# Physics

Magnetic hysteresis describes the lag between applied magnetic field and magnetization response.

The magnetization response is represented as:

$$
M = \chi H
$$

where:

- $M$ = magnetization
- $\chi$ = magnetic susceptibility
- $H$ = applied magnetic field

The magnetic interactions are modeled using the Heisenberg Hamiltonian:

$$
H = -\sum_{ij} J_{ij}\,\vec{S}_i \cdot \vec{S}_j
$$

where:

- $J_{ij}$ = exchange interaction
- $\vec{S}_i$, $\vec{S}_j$ = neighboring spins

The simulation studies magnetization evolution under cyclic external magnetic fields.

---

# Features

- Magnetic hysteresis loop simulations
- Magnetization-field response
- Spin interaction modeling
- Magnetic relaxation behavior
- Visualization of hysteresis curves

---

# Repository Structure

```text
hysteresis-loop-simulation/

├── Fe.mat
├── input
├── plot.py
├── run.sh
├── README.md
├── output/
└── log/
```

---

# Requirements

- Python 3.x
- NumPy
- Matplotlib
- VAMPIRE Atomistic Spin Dynamics package

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Simulation

Run the simulation:

```bash
bash run.sh
```

Generate plots:

```bash
python plot.py
```

---

# Outputs

The simulation generates:

- Magnetization curves
- Hysteresis loops
- Magnetic response plots
- Field-dependent magnetization behavior

---

# Learning Objectives

This project was developed to explore:

- Magnetic hysteresis
- Ferromagnetic behavior
- Spin interactions
- Numerical simulation methods
- Magnetization dynamics
- Computational condensed matter physics

---

# References

- Classical Heisenberg model
- Magnetic hysteresis theory
- Atomistic spin dynamics
- VAMPIRE simulation package

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
