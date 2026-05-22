import matplotlib.pyplot as plt
import numpy as np


def plot_complex_spectrum(eigenvalues, filename):

    plt.figure(figsize=(7,7))

    plt.scatter(
        eigenvalues.real,
        eigenvalues.imag,
        s=20
    )

    plt.xlabel('Re(E)')
    plt.ylabel('Im(E)')

    plt.title('Complex Energy Spectrum')

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(filename, dpi=300)

    plt.close()


def plot_edge_state(probability, filename):

    plt.figure(figsize=(8,5))

    plt.plot(
        probability,
        linewidth=2
    )

    plt.xlabel('Site Index')

    plt.ylabel(r'$|\psi|^2$')

    plt.title('Edge State Localization')

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(filename, dpi=300)

    plt.close()
