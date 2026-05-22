# Magnon Dynamics Using VAMPIRE

Exploratory atomistic spin dynamics simulations of magnons and spin-wave excitations using the VAMPIRE atomistic simulation package.

This project was developed for learning, numerical experimentation, and research training in computational condensed matter physics and magnetic dynamics.

---

# Physics

The spin dynamics are governed by the Landau-Lifshitz-Gilbert (LLG) equation:

$$
\frac{d\vec{S}}{dt} = -\gamma \vec{S} \times \vec{H}_{\mathrm{eff}} + \alpha \vec{S} \times \frac{d\vec{S}}{dt}
$$

where:

- $\vec{S}$ = atomic spin vector
- $\gamma$ = gyromagnetic ratio
- $\alpha$ = damping constant
- $\vec{H}_{\mathrm{eff}}$ = effective magnetic field

The magnetic interactions are modeled using the Heisenberg Hamiltonian:

$$
H = -\sum_{ij} J_{ij}\,\vec{S}_i \cdot \vec{S}_j
$$

Spin-wave excitations generate magnons with characteristic dispersion relations:

$$
\omega(k) \propto J\left(1 - \cos(ka)\right)
$$

where:

- $\omega(k)$ = magnon frequency
- $k$ = wave vector
- $a$ = lattice spacing

---

# Features

- Atomistic spin dynamics simulations
- Magnon excitation analysis
- Spin-wave dynamics
- Magnetization evolution
- Frequency-domain analysis
- VAMPIRE-based simulations

---

# Repository Structure

```text
magnon-dynamics-using-vampire/

├── Fe.mat
├── input
├── plot.py
├── run.sh
├── magnon_dynamics.png
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

Run the VAMPIRE simulation:

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

- Magnon spectra
- Magnetization dynamics
- Spin-wave evolution
- Time-dependent magnetic behavior
- Frequency-domain magnetic response

Representative outputs include:

- `magnon_dynamics.png`

---

# Learning Objectives

This project was developed to explore:

- Magnon physics
- Spin-wave excitations
- Atomistic spin dynamics
- Frequency-domain analysis
- Magnetic many-body systems
- Computational condensed matter physics

---

# References

- VAMPIRE Atomistic Spin Dynamics Software
- Landau-Lifshitz-Gilbert equation
- Spin-wave theory
- Heisenberg model
- Magnon dynamics in ferromagnets

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
