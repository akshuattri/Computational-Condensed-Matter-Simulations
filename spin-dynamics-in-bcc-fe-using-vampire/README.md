# Spin Dynamics in BCC Fe Using VAMPIRE

Exploratory atomistic spin dynamics simulations of body-centered cubic (BCC) iron using the VAMPIRE atomistic simulation package.

This project was developed for learning, numerical experimentation, and research training in computational condensed matter physics and magnetization dynamics.

---

## Physics

The spin dynamics are governed by the Landau-Lifshitz-Gilbert (LLG) equation:

$$
\frac{d\vec{S}}{dt} = -\gamma \vec{S} \times \vec{H}_{\mathrm{eff}} + \alpha \vec{S} \times \frac{d\vec{S}}{dt}
$$

where:

- $\vec{S}$ = atomic spin vector
- $\gamma$ = gyromagnetic ratio
- $\alpha$ = damping constant
- $\vec{H}_{\mathrm{eff}}$ = effective magnetic field

The magnetic interactions are described using the Heisenberg Hamiltonian:

$$
H = -\sum_{ij} J_{ij}\,\vec{S}_i \cdot \vec{S}_j
$$

where:

- $J_{ij}$ = exchange interaction
- $\vec{S}_i$, $\vec{S}_j$ = neighboring atomic spins

---

# Features

- Atomistic spin dynamics simulations
- Magnetization dynamics in BCC Fe
- Time evolution of magnetic moments
- Magnetization component analysis
- Spin precession and damping
- Frequency-domain magnetic behavior
- VAMPIRE-based simulations

---

# Repository Structure

```text
spin-dynamics-in-bcc-fe-using-vampire/

├── Fe.mat
├── input
├── plot.py
├── run.sh
├── README.md
├── magnetization_components.png
├── magnetization_magnitude.png
├── output/
└── log/
```

---

# Requirements

- Python 3.x
- NumPy
- Matplotlib
- VAMPIRE Atomistic Spin Dynamics package

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Simulation

Run the VAMPIRE simulation:

```bash
bash run.sh
```

Plot the generated data:

```bash
python plot.py
```

---

# Outputs

The simulation generates:

- Magnetization dynamics
- Spin component evolution
- Magnetization magnitude plots
- Time-dependent magnetic response

Representative outputs:

- `magnetization_components.png`
- `magnetization_magnitude.png`

---

# Learning Objectives

This project was developed to explore:

- Atomistic spin dynamics
- Magnetic relaxation processes
- Heisenberg exchange interactions
- Numerical simulation techniques
- Magnetization dynamics in ferromagnets
- Computational condensed matter physics

---

# References

- VAMPIRE Atomistic Spin Dynamics Software
- Landau-Lifshitz-Gilbert equation
- Classical Heisenberg model
- Spin dynamics simulations in ferromagnetic materials

---

# Disclaimer

This repository is intended for educational, exploratory, and research-learning purposes.
