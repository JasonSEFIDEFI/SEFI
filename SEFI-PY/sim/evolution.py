# sim/evolution.py

from utils.geometry import normalize

def evolve_position(entity, dt=0.1):
    """
    Update entity position based on its momentum.
    """
    px, py, pz = entity.origin.position
    mx, my, mz = entity.origin.momentum

    entity.origin.position = [
        px + mx * dt,
        py + my * dt,
        pz + mz * dt
    ]

def evolve_momentum(entity, dt=0.1):
    """
    Update momentum based on DEFI intensity and expression direction.
    """
    intensity = entity.defi.defi_intensity()
    direction = normalize(entity.expression.expression_vector())

    dx, dy, dz = direction

    entity.origin.momentum = [
        entity.origin.momentum[0] + dx * intensity * dt,
        entity.origin.momentum[1] + dy * intensity * dt,
        entity.origin.momentum[2] + dz * intensity * dt
    ]
