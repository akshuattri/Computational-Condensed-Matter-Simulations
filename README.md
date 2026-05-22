# Computational Condensed Matter Simulations

Exploratory computational condensed matter simulations developed for learning, numerical experimentation, and research training in spin dynamics, quantum transport, non-Hermitian systems, and many-body physics.

This repository is a collection of simulation projects focused on understanding numerical methods and physical models commonly used in computational condensed matter research.

---

# Topics Covered

- Spin dynamics
- Quantum transport
- Green's function methods
- Monte Carlo simulations
- Non-Hermitian systems
- Tight-binding Hamiltonians
- Magnon dynamics
- Spin-wave analysis
- Topological systems
- Atomistic simulations

---

# Repository Structure

```text
Computational-Condensed-Matter-Simulations/

├── fe-herisenberg-montecarlo/
├── frequency-domain-spin-wave-analysis/
├── hysteresis-loop-simulation/
├── ising_mote_carlo/
├── levy-fe-heisenberg/
├── magnon-dynamics-using-vampire/
├── non-hermitian-tightbinding/
├── quantum-transport-greenfunctions/
└── spin-dynamics-in-bcc-fe-using-vampire/
```

---

# Projects

| Project | Description |
|---|---|
| `fe-herisenberg-montecarlo` | Monte Carlo simulations using the classical Heisenberg model |
| `frequency-domain-spin-wave-analysis` | Frequency-domain analysis of spin-wave excitations and magnon spectra |
| `hysteresis-loop-simulation` | Magnetic hysteresis simulations and magnetization dynamics |
| `ising_mote_carlo` | Ising model simulations using Metropolis Monte Carlo methods |
| `levy-fe-heisenberg` | Heisenberg spin simulations and thermal magnetic behavior |
| `magnon-dynamics-using-vampire` | Atomistic magnon and spin-wave dynamics using VAMPIRE |
| `non-hermitian-tightbinding` | Non-Hermitian tight-binding and edge-state simulations |
| `quantum-transport-greenfunctions` | Quantum transport calculations using Green's function methods |
| `spin-dynamics-in-bcc-fe-using-vampire` | Atomistic spin dynamics simulations in BCC iron |

---

# Physics Models

The repository includes implementations and exploratory studies based on:

## Heisenberg Hamiltonian

$$
H = -\sum_{ij} J_{ij}\,\vec{S}_i \cdot \vec{S}_j
$$

## Ising Model

$$
H = -J \sum_{\langle i,j \rangle} S_i S_j
$$

## Landau-Lifshitz-Gilbert Equation

$$
\frac{d\vec{S}}{dt} = -\gamma \vec{S} \times \vec{H}_{\mathrm{eff}} + \alpha \vec{S} \times \frac{d\vec{S}}{dt}
$$

## Green's Function Formalism

$$
G^R(E) = \left[E I - H - \Sigma_L - \Sigma_R \right]^{-1}
$$

---

# Tools & Methods

- Python
- NumPy
- SciPy
- Matplotlib
- Tight-binding methods
- Monte Carlo algorithms
- Fourier analysis
- Atomistic spin dynamics
- Green's function techniques
- VAMPIRE simulation package

---

# Learning Objectives

The primary goal of this repository is to explore:

- Numerical simulation techniques
- Computational condensed matter physics
- Magnetic many-body systems
- Quantum transport phenomena
- Statistical mechanics
- Spin dynamics and magnon physics
- Topological and non-Hermitian systems

---

# Disclaimer

These projects are exploratory implementations developed primarily for educational, learning, and research-training purposes.

---

# References

- Classical Heisenberg model
- Ising model
- Green's function methods
- Landau-Lifshitz-Gilbert dynamics
- Monte Carlo methods in statistical physics
- Tight-binding models
- Computational condensed matter physics
- Atomistic spin dynamics
