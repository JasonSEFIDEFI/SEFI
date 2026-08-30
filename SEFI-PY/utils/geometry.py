# utils/geometry.py

import math

def magnitude(vec):
    return math.sqrt(sum(v*v for v in vec))

def normalize(vec):
    mag = magnitude(vec)
    return [v / mag for v in vec] if mag != 0 else [0.0 for v in vec]

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

def project(a, b):
    denom = dot(b, b)
    if denom == 0:
        return [0 for _ in b]
    scale = dot(a, b) / denom
    return [scale * x for x in b]
