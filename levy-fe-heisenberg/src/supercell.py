import numpy as np

def build_supercell(lattice, positions, n):

    all_positions = []

    for i in range(n):
        for j in range(n):
            for k in range(n):

                shift = np.array([i,j,k])

                for pos in positions:

                    new_pos = pos + shift

                    cart = new_pos @ lattice

                    all_positions.append(cart)

    return np.array(all_positions)
