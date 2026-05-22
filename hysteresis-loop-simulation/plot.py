import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('output', comments='#')

H = data[:,0]
Mz = data[:,3]

bins = np.linspace(H.min(), H.max(), 60)

digitized = np.digitize(H, bins)

H_avg = []
M_avg = []

for i in range(1, len(bins)):

    mask = digitized == i

    if np.any(mask):

        H_avg.append(np.mean(H[mask]))

        M_avg.append(np.mean(Mz[mask]))

plt.figure(figsize=(8,6))

plt.plot(
    H_avg,
    M_avg,
    'o-',
    linewidth=2
)

plt.xlabel('Applied Magnetic Field')

plt.ylabel('Magnetization')

plt.title('BCC Fe Hysteresis Loop')

plt.grid(True)

plt.tight_layout()

plt.savefig(
    'hysteresis_loop.png',
    dpi=300
)

plt.show()
