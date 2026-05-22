import matplotlib.pyplot as plt

def plot_quantity(
    x,
    y,
    xlabel,
    ylabel,
    filename
):

    plt.figure(figsize=(8,6))

    plt.plot(
        x,
        y,
        'o-',
        linewidth=2
    )

    plt.xlabel(xlabel)

    plt.ylabel(ylabel)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(filename, dpi=300)

    plt.close()
