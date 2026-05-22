import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
    'output',
    comments='#'
)

Mx = data[:,1]

My = data[:,2]

Mz = data[:,3]

M = data[:,4]

steps = np.arange(len(M))

plt.figure(figsize=(10,6))

plt.plot(
    steps,
    Mx,
    label='Mx'
)

plt.plot(
    steps,
    My,
    label='My'
)

plt.plot(
    steps,
    Mz,
    label='Mz'
)

plt.xlabel('Simulation Step')

plt.ylabel('Magnetization Components')

plt.title('Magnon Dynamics in BCC Fe')

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    'magnon_dynamics.png',
    dpi=300
)

plt.show()
