# Frequency Domain Spin Wave Analysis

Exploratory simulations and frequency-domain analysis of spin-wave excitations and magnon dynamics in magnetic systems.

This project was developed for learning, numerical experimentation, and research training in computational condensed matter physics and spin dynamics.

---

# Physics

Spin waves are collective excitations of interacting magnetic moments in ordered magnetic materials.

The spin-wave dispersion relation can be approximated as:

$$
\omega(k) \propto J\left(1 - \cos(ka)\right)
$$

where:

- $\omega(k)$ = spin-wave frequency
- $J$ = exchange interaction
- $k$ = wave vector
- $a$ = lattice spacing

Frequency-domain analysis is performed using Fourier transforms:

$$
S(\omega) = \int s(t)e^{-i\omega t}dt
$$

where:

- $s(t)$ = time-dependent spin signal
- $S(\omega)$ = frequency spectrum

The magnetic interactions are described using the Heisenberg Hamiltonian:

$$
H = -\sum_{ij} J_{ij}\,\vec{S}_i \cdot \vec{S}_j
$$

---

# Features

- Frequency-domain spin-wave analysis
- Magnon spectrum calculations
- Fourier transform analysis
- Magnetization dynamics
- Spin-wave mode visualization
- Spectral analysis of magnetic excitations

---

# Repository Structure

```text
frequency-domain-spin-wave-analysis/

├── Fe.mat
├── input
├── plot.py
├── run.sh
├── magnon_spectrum.png
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

Run the spin dynamics simulation:

```bash
bash run.sh
```

Generate spectral plots:

```bash
python plot.py
```

---

# Outputs

The simulation generates:

- Magnon spectra
- Frequency-domain response
- Spin-wave dispersion information
- Spectral intensity plots

Representative output:

- `magnon_spectrum.png`

---

# Learning Objectives

This project was developed to explore:

- Spin-wave physics
- Magnon excitations
- Fourier transform methods
- Frequency-domain analysis
- Magnetization dynamics
- Computational condensed matter physics

---

# References

- Spin-wave theory
- Magnon dynamics
- Fourier spectral analysis
- Heisenberg model
- Atomistic spin dynamics

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
