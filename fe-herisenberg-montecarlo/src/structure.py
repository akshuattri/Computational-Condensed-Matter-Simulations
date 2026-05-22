import numpy as np

def read_poscar(filename):

    with open(filename, 'r') as f:

        lines = f.readlines()

    scale = float(lines[1])

    lattice = np.array([
        list(map(float, lines[2].split())),
        list(map(float, lines[3].split())),
        list(map(float, lines[4].split()))
    ]) * scale

    natoms = int(lines[6].split()[0])

    positions = []

    for i in range(natoms):

        pos = list(map(float, lines[8 + i].split()[:3]))

        positions.append(pos)

    positions = np.array(positions)

    return lattice, positions
