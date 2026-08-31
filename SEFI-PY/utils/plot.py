import numpy as np
import matplotlib.pyplot as plt


def plot_response(worldline, engine, t_min=0.0, t_max=10.0, n=500):
    """
    Plot curvature and torsion response of a warped worldline.

    engine.response(t) must return:
        (k_original, k_warped, τ_original, τ_warped)
    """

    ts = np.linspace(t_min, t_max, n)

    k0, k1 = [], []
    t0, t1 = [], []

    for t in ts:
        r = engine.response(t)
        k0.append(r[0])
        k1.append(r[1])
        t0.append(r[2])
        t1.append(r[3])

    plt.figure(figsize=(10, 5))

    # Curvature subplot
    plt.subplot(1, 2, 1)
    plt.plot(ts, k0, label="κ original", linewidth=2.0)
    plt.plot(ts, k1, label="κ warped", linewidth=2.0)
    plt.title("Curvature")
    plt.xlabel("t")
    plt.ylabel("κ(t)")
    plt.legend()

    # Torsion subplot
    plt.subplot(1, 2, 2)
    plt.plot(ts, t0, label="τ original", linewidth=2.0)
    plt.plot(ts, t1, label="τ warped", linewidth=2.0)
    plt.title("Torsion")
    plt.xlabel("t")
    plt.ylabel("τ(t)")
    plt.legend()

    plt.tight_layout()
    plt.show()
