import numpy as np

def build_neighbor_list(positions, cutoff):

    neighbors = []

    N = len(positions)

    for i in range(N):

        local_neighbors = []

        for j in range(N):

            if i == j:
                continue

            rij = positions[j] - positions[i]

            dist = np.linalg.norm(rij)

            if dist < cutoff:

                local_neighbors.append(j)

        neighbors.append(local_neighbors)

    return neighbors
