def clamp(value, low, high):
    return max(low, min(value, high))

def stable_ratio(a, b, eps=1e-9):
    """Return a stable ratio a/b with epsilon protection."""
    return a / (b if abs(b) > eps else eps)

def blend(a, b, t):
    """Linear blend with clamped t."""
    t = clamp(t, 0.0, 1.0)
    return (1 - t) * a + t * b
