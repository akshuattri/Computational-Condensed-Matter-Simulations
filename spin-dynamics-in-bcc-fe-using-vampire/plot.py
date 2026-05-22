import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
    'output',
    comments='#'
)

temperature = data[:,0]

Mx = data[:,1]

My = data[:,2]

Mz = data[:,3]

M = data[:,4]


plt.figure(figsize=(8,6))

plt.plot(Mx, label='Mx')

plt.plot(My, label='My')

plt.plot(Mz, label='Mz')

plt.xlabel('Simulation Step')

plt.ylabel('Magnetization Components')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    'magnetization_components.png',
    dpi=300
)

plt.close()

plt.figure(figsize=(8,6))

plt.plot(
    M,
    linewidth=2
)

plt.xlabel('Simulation Step')

plt.ylabel('|M|')

plt.grid(True)

plt.tight_layout()

plt.savefig(
    'magnetization_magnitude.png',
    dpi=300
)

plt.close()

print('Plots generated successfully.')
