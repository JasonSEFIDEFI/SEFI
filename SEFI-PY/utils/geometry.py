import numpy as np

# ---------------------------------------------------------
# Basic vector operations
# ---------------------------------------------------------

def magnitude(vec):
    """
    Return the Euclidean norm of a vector.
    """
    vec = np.asarray(vec)
    return np.linalg.norm(vec)


def normalize(vec):
    """
    Return the unit vector in the direction of vec.
    """
    vec = np.asarray(vec)
    mag = np.linalg.norm(vec)
    if mag == 0:
        return np.zeros_like(vec)
    return vec / mag


def dot(a, b):
    """
    Dot product of two vectors.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    return float(np.dot(a, b))


def project(a, b):
    """
    Project vector a onto vector b.
    """
    a = np.asarray(a)
    b = np.asarray(b)
    denom = np.dot(b, b)
    if denom == 0:
        return np.zeros_like(b)
    scale = np.dot(a, b) / denom
    return scale * b


# ---------------------------------------------------------
# Frenet–Serret frame
# ---------------------------------------------------------

def frenet_frame(worldline, t):
    """
    Compute Frenet–Serret frame (T, N, B) for a given worldline at parameter t.

    T : unit tangent
    N : unit normal
    B : binormal
    """
    v = worldline.v(t)
    a = worldline.a(t)

    T = normalize(v)
    N = normalize(a)
    B = np.cross(T, N)

    return T, N, B
