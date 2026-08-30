from utils.geometry import normalize, dot, magnitude

def test_normalize_vector():
    v = [3.0, 4.0, 0.0]
    n = normalize(v)
    assert round(magnitude(n), 5) == 1.0

def test_dot_product():
    assert dot([1, 0, 0], [1, 0, 0]) == 1
    assert dot([1, 0, 0], [0, 1, 0]) == 0

def test_magnitude():
    assert magnitude([3, 4, 0]) == 5
