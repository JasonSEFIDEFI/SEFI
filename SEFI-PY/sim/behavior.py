# sim/behavior.py

from utils.geometry import normalize, dot

def compute_drive(entity):
    """
    DRIVE:
    The entity's internal push to act.
    Based on DEFI intensity and sovereignty alignment.
    """
    defi = entity.defi.defi_intensity()
    align = entity.sovereignty.sovereignty_alignment()
    return defi * (0.5 + 0.5 * align)


def compute_orientation(entity):
    """
    ORIENTATION:
    The direction the entity prefers to move.
    Weighted blend of:
    - sovereignty vector (identity persistence)
    - expression vector (active projection)
    """
    sov = entity.sovereignty.sovereignty_vector()
    exp = entity.expression.expression_vector()

    # 60% sovereignty, 40% expression
    return normalize([0.6*s + 0.4*e for s, e in zip(sov, exp)])


def apply_behavior(entity, dt=0.1):
    """
    Apply behavior to momentum.
    DRIVE determines magnitude.
    ORIENTATION determines direction.
    """
    drive = compute_drive(entity)
    orient = compute_orientation(entity)

    ox, oy, oz = orient

    entity.origin.momentum[0] += ox * drive * dt
    entity.origin.momentum[1] += oy * drive * dt
    entity.origin.momentum[2] += oz * drive * dt
