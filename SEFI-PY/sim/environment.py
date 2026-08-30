# sim/environment.py

from utils.geometry import normalize, magnitude

class Environment:
    """
    SEFI-SIM environment:
    - global field direction
    - boundary constraints
    - ambient influence
    """

    def __init__(
        self,
        global_field=[0.0, 0.0, 0.0],
        boundary_radius=10.0,
        ambient_intensity=0.1
    ):
        self.global_field = global_field
        self.boundary_radius = boundary_radius
        self.ambient_intensity = ambient_intensity

    def apply_global_field(self, entity, dt=0.1):
        """
        Global field nudges momentum in a fixed direction.
        """
        gf = normalize(self.global_field) if magnitude(self.global_field) > 0 else [0.0, 0.0, 0.0]
        gx, gy, gz = gf

        entity.origin.momentum[0] += gx * self.ambient_intensity * dt
        entity.origin.momentum[1] += gy * self.ambient_intensity * dt
        entity.origin.momentum[2] += gz * self.ambient_intensity * dt

    def apply_boundary(self, entity, dt=0.1):
        """
        Soft boundary: if entity moves too far from origin,
        gently push it back.
        """
        px, py, pz = entity.origin.position
        dist = magnitude([px, py, pz])

        if dist <= self.boundary_radius:
            return

        # direction back toward origin
        direction_back = normalize([-px, -py, -pz])
        bx, by, bz = direction_back

        # strength increases with distance beyond boundary
        excess = dist - self.boundary_radius
        strength = 0.2 * excess

        entity.origin.momentum[0] += bx * strength * dt
        entity.origin.momentum[1] += by * strength * dt
        entity.origin.momentum[2] += bz * strength * dt
