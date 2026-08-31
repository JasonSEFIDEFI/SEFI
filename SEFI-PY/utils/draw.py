import numpy as np
import matplotlib.pyplot as plt

def draw_1d(worldline, t_min=0.0, t_max=10.0, n=500):
    """
    Draw the 1D x(t) projection of a worldline r(t).

    Parameters
    ----------
    worldline : Worldline
        The SEFI-PY worldline object with r(t) -> R^3.
    t_min : float
        Start time.
    t_max : float
        End time.
    n : int
        Number of samples.

    Produces
    --------
    A matplotlib plot of x(t) vs t.
    """
    ts = np.linspace(t_min, t_max, n)
    xs = [worldline.r(t)[0] for t in ts]

    plt.figure(figsize=(8, 4))
    plt.plot(ts, xs, linewidth=2.0)
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.title("1D Projection of Worldline")
    plt.tight_layout()
    plt.show()
