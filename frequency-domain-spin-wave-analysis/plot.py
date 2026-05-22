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

plt.close()

signal = Mx - np.mean(Mx)

fft_vals = np.fft.fft(signal)

freqs = np.fft.fftfreq(
    len(signal),
    d=1.0e-15
)

power = np.abs(fft_vals)**2

mask = freqs > 0

plt.figure(figsize=(10,6))

plt.plot(
    freqs[mask],
    power[mask],
    linewidth=2
)

plt.xlabel('Frequency (Hz)')

plt.ylabel('FFT Power')

plt.title('Magnon Frequency Spectrum')

plt.grid(True)

plt.tight_layout()

plt.savefig(
    'magnon_spectrum.png',
    dpi=300
)

plt.close()

print('Magnon dynamics and FFT spectrum generated.')
