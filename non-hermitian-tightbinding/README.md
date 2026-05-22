# Non-Hermitian SSH Model

Exploratory simulations of the non-Hermitian Su-Schrieffer-Heeger (SSH) model for studying topological phases, edge states, and complex energy spectra in condensed matter systems.

This project was developed for learning, numerical experimentation, and research training in non-Hermitian quantum mechanics and topological condensed matter physics.

---

# Physics

The non-Hermitian SSH model is described using a tight-binding Hamiltonian with asymmetric hopping amplitudes:

$$
H = \sum_n (t_1 + \gamma)c_{n,A}^\dagger c_{n,B} + (t_2 - \gamma)c_{n+1,A}^\dagger c_{n,B} + h.c.
$$

where:

- $t_1$, $t_2$ = intracell and intercell hopping amplitudes
- $\gamma$ = non-Hermitian asymmetry parameter
- $c^\dagger$, $c$ = fermionic creation and annihilation operators

The system satisfies:

$$
H \neq H^\dagger
$$

leading to:

- complex eigenvalue spectra
- non-Hermitian skin effects
- topological edge localization

The energy spectrum is obtained from:

$$
H|\psi_n\rangle = E_n|\psi_n\rangle
$$

where complex eigenvalues $E_n$ characterize the non-Hermitian phases.

---

# Features

- Non-Hermitian SSH Hamiltonian
- Complex eigenvalue spectrum
- Edge-state localization
- Open and periodic boundary conditions
- Topological phase analysis
- Non-Hermitian skin effect simulations

---

# Repository Structure

```text
non-hermitian-ssh-simulator/

├── input.dat
├── run.py
├── requirements.txt
├── README.md
├── src/
├── figures/
│   ├── edge_states.png
│   └── complex_spectrum.png
```

---

# Requirements

- Python 3.x
- NumPy
- SciPy
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

- Complex energy spectra
- Edge-state probability distributions
- Localization profiles
- Topological phase visualizations

Representative outputs include:

- `edge_states.png`
- `complex_spectrum.png`

---

# Learning Objectives

This project was developed to explore:

- Non-Hermitian quantum mechanics
- Topological phases
- SSH tight-binding models
- Edge-state physics
- Complex spectra
- Numerical diagonalization methods

---

# References

- Su-Schrieffer-Heeger (SSH) model
- Non-Hermitian topology
- Topological edge states
- Tight-binding Hamiltonians
- Computational condensed matter physics

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
