# sim/world.py

from sim.environment import Environment
import numpy as np


# ---------------------------------------------------------
# SEFI-SIM World Container
# ---------------------------------------------------------

class World:
    """
    The SEFI simulation world:
    - holds entities
    - applies environment effects
    - steps entity evolution
    """

    def __init__(self, global_field=[0.0, 0.0, 0.0],
                 boundary_radius=10.0,
                 ambient_intensity=0.1):

        self.entities = []
        self.environment = Environment(
            global_field=global_field,
            boundary_radius=boundary_radius,
            ambient_intensity=ambient_intensity
        )

    def add(self, entity):
        self.entities.append(entity)

    def step(self, dt=0.1):
        """
        Full world evolution step:
        - environment effects
        - entity evolution
        """
        for e in self.entities:
            self.environment.apply_global_field(e, dt)
            self.environment.apply_boundary(e, dt)
            e.step(dt)


# ---------------------------------------------------------
# SEFI-PY Worldline Geometry
# ---------------------------------------------------------

class Worldline:
    """
    Parametric worldline r(t) in R^3 with curvature and torsion.
    Backbone of SEFI geometry.
    """

    def __init__(self, r_func):
        self.r = r_func

    # -----------------------------------------------------
    # Numerical derivatives (central finite differences)
    # -----------------------------------------------------
    def _derivative(self, t, order=1, dt=1e-5):
        if order == 1:
            return (self.r(t + dt) - self.r(t - dt)) / (2 * dt)

        if order == 2:
            return (self.r(t + dt) - 2*self.r(t) + self.r(t - dt)) / (dt**2)

        if order == 3:
            return (self.r(t + 2*dt)
                    - 3*self.r(t + dt)
                    + 3*self.r(t - dt)
                    - self.r(t - 2*dt)) / (2 * dt**3)

        raise ValueError("Order must be 1, 2, or 3.")

    # -----------------------------------------------------
    # Frenet–Serret components
    # -----------------------------------------------------
    def v(self, t):
        return self._derivative(t, order=1)

    def a(self, t):
        return self._derivative(t, order=2)

    def j(self, t):
        return self._derivative(t, order=3)

    # -----------------------------------------------------
    # Curvature κ(t)
    # -----------------------------------------------------
    def curvature(self, t):
        v = self.v(t)
        a = self.a(t)
        cross = np.cross(v, a)
        return np.linalg.norm(cross) / np.linalg.norm(v)**3

    # -----------------------------------------------------
    # Torsion τ(t)
    # -----------------------------------------------------
    def torsion(self, t):
        v = self.v(t)
        a = self.a(t)
        j = self.j(t)

        num = np.linalg.det(np.vstack([v, a, j]))
        den = np.linalg.norm(np.cross(v, a))**2

        return num / den

    # -----------------------------------------------------
    # Frenet–Serret frame (T, N, B)
    # -----------------------------------------------------
    def frenet_frame(self, t):
        v = self.v(t)
        a = self.a(t)

        T = v / np.linalg.norm(v)
        N = a / np.linalg.norm(a)
        B = np.cross(T, N)

        return T, N, B
