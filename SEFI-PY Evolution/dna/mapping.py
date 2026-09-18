import numpy as np

def sequence_to_curvature(sequence_vectors: list) -> list:
    """
    Maps sequence transition vectors directly to local curvature (kappa) dynamics.
    """
    curvatures = []
    for vec in sequence_vectors:
        kappa = np.sum(vec) * 0.25
        curvatures.append(kappa)
    return curvatures