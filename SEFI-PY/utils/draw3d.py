import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_3d(worldline, t_min=0.0, t_max=10.0, n=500,
            title="3D Worldline"):
    """
    Draw a 3D parametric worldline r(t) = (x(t), y(t), z(t)).

    Parameters
    ----------
    worldline : Worldline
        SEFI-PY worldline object with r(t) -> R^3.
    t_min : float
        Start time.
    t_max : float
        End time.
    n : int
        Number of samples.
    title : str
        Plot title.

    Produces
    --------
    A 3D matplotlib plot of the worldline.
    """

    ts = np.linspace(t_min, t_max, n)
    xs, ys, zs = [], [], []

    for t in ts:
        r = worldline.r(t)
        xs.append(r[0])
        ys.append(r[1])
        zs.append(r[2])

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(xs, ys, zs, linewidth=2.0)

    ax.set_xlabel("x(t)")
    ax.set_ylabel("y(t)")
    ax.set_zlabel("z(t)")
    ax.set_title(title)

    plt.tight_layout()
    plt.show()
