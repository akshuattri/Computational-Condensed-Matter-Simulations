# Quantum Transport Green Functions

Exploratory simulations of quantum transport phenomena using Green's function methods and tight-binding Hamiltonians.

This project was developed for learning, numerical experimentation, and research training in computational condensed matter physics and mesoscopic quantum transport.

---

# Physics

Quantum transport is described using the retarded Green's function:

$$
G^R(E) = \left[E I - H - \Sigma_L - \Sigma_R \right]^{-1}
$$

where:

- $E$ = energy
- $H$ = system Hamiltonian
- $\Sigma_L$, $\Sigma_R$ = self-energy terms from contacts
- $G^R(E)$ = retarded Green's function

The transmission function is computed as:

$$
T(E) = \mathrm{Tr}\left[\Gamma_L G^R \Gamma_R G^A \right]
$$

where:

- $\Gamma_L$, $\Gamma_R$ = coupling matrices
- $G^A$ = advanced Green's function

The system Hamiltonian is modeled using a tight-binding formalism:

$$
H = \sum_i \epsilon_i c_i^\dagger c_i + \sum_{ij} t_{ij} c_i^\dagger c_j
$$

where:

- $\epsilon_i$ = onsite energy
- $t_{ij}$ = hopping amplitude

---

# Features

- Green's function transport calculations
- Tight-binding Hamiltonians
- Density of states calculations
- Transmission spectrum analysis
- Quantum conductance simulations
- Energy-resolved transport properties

---

# Repository Structure

```text
quantum-transport-greenfunctions/

├── input.dat
├── run.py
├── requirements.txt
├── README.md
├── src/
│   ├── greens.py
│   ├── hamiltonian.py
│   ├── observables.py
│   ├── plotting.py
│   └── transport.py
├── figures/
│   ├── dos.png
│   └── transmission.png
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

Run the transport simulation:

```bash
python run.py
```

---

# Outputs

The simulation generates:

- Transmission spectra
- Density of states plots
- Energy-dependent conductance
- Quantum transport observables

Representative outputs include:

- `dos.png`
- `transmission.png`

---

# Learning Objectives

This project was developed to explore:

- Green's function formalism
- Quantum transport theory
- Tight-binding methods
- Mesoscopic systems
- Numerical linear algebra
- Computational condensed matter physics

---

# References

- Non-equilibrium Green's function formalism
- Tight-binding models
- Quantum transport theory
- Mesoscopic physics
- Computational condensed matter methods

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
