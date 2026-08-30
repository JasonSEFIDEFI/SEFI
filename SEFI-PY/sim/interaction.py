# sim/interaction.py

from utils.geometry import normalize, magnitude

def apply_interaction(entity_a, entity_b, dt=0.1):
    """
    Entities influence each other's momentum based on proximity
    and sovereignty strength.
    """

    ax, ay, az = entity_a.origin.position
    bx, by, bz = entity_b.origin.position

    # vector from A to B
    direction = [bx - ax, by - ay, bz - az]
    dist = magnitude(direction)

    if dist == 0:
        return  # avoid division by zero

    direction = normalize(direction)

    # influence strength based on sovereignty
    influence = entity_a.sovereignty.sovereignty_strength() / (dist + 1.0)

    # apply influence to B's momentum
    entity_b.origin.momentum[0] += direction[0] * influence * dt
    entity_b.origin.momentum[1] += direction[1] * influence * dt
    entity_b.origin.momentum[2] += direction[2] * influence * dt
