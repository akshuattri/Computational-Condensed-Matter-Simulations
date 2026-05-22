# Spin Dynamics in BCC Fe using VAMPIRE

Atomistic spin dynamics simulation of ferromagnetic BCC Fe using the VAMPIRE atomistic spin simulation framework.

This project demonstrates:
- atomistic Heisenberg spin simulations
- Landau-Lifshitz-Gilbert (LLG) spin dynamics
- magnetic relaxation
- thermal spin fluctuations
- computational condensed matter physics workflows

---

# Physics

The spin dynamics are governed by the Landau-Lifshitz-Gilbert (LLG) equation:

$$
\frac{d\vec S}{dt}
=
-\gamma \vec S \times \vec H_{eff}
+
\alpha \vec S \times \frac{d\vec S}{dt}
$$

where:
- $\vec S$ = atomic spin vector
- $\gamma$ = gyromagnetic ratio
- $\alpha$ = damping constant
- $\vec H_{eff}$ = effective magnetic field

The magnetic interactions are described using the Heisenberg Hamiltonian:

$$
H
=
-\sum_{ij}
J_{ij}
\vec S_i \cdot \vec S_j
$$

---

# Features

- BCC Fe crystal structure
- Atomistic spin dynamics
- Heisenberg exchange interactions
- Magnetic anisotropy
- Time evolution of magnetization
- Magnetization component analysis
- Automated plotting workflow

---

# Software Used

- VAMPIRE
- Python
- NumPy
- Matplotlib

---

# Repository Structure

```text
spin-dynamics-in-bcc-fe-using-vampire/
│
├── input
├── Fe.mat
├── run.sh
├── plot.py
├── output
├── log
│
├── magnetization_components.png
├── magnetization_magnitude.png
│
└── README.md
```

---

# Simulation Parameters

| Parameter | Value |
|---|---|
| Material | BCC Fe |
| Lattice Constant | 2.866 Å |
| System Size | 8 × 8 × 8 |
| Temperature | 300 K |
| Time Step | 1 fs |
| Total Time Steps | 50000 |
| Spin Moment | 2.2 μB |

---

# Running the Simulation

## Compile VAMPIRE

```bash
make -j4
```

---

## Run Spin Dynamics

```bash
./run.sh
```

---

## Generate Plots

```bash
python3 plot.py
```

---

# Results

The simulation generates:
- magnetization evolution
- magnetization component dynamics
- spin relaxation behavior

Example outputs:
- `magnetization_components.png`
- `magnetization_magnitude.png`

---

# Example Workflow

```bash
./run.sh
python3 plot.py
```

---

# Computational Methods

The project uses:
- atomistic spin dynamics
- LLG integration
- stochastic thermal fluctuations
- Heisenberg exchange coupling

implemented internally using the VAMPIRE simulation engine.

---

# Future Extensions

Possible future upgrades:
- Curie temperature simulations
- Monte Carlo thermodynamics
- ultrafast magnetic switching
- non-Hermitian spin dynamics
- ferrimagnetic materials
- applied magnetic fields
- spin-wave analysis

---

# Research Relevance

This project is relevant for:
- computational magnetism
- spintronics
- condensed matter physics
- atomistic simulations
- magnetic materials modeling
- ultrafast magnetization dynamics

---

# Author

Akshu Attri

Computational Condensed Matter Physics  
Monte Carlo Simulations | Spin Dynamics | Quantum Materials
