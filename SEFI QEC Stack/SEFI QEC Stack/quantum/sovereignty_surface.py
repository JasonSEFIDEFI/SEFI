import math


def sovereignty_distance(phi):

    return math.sqrt(
        phi.x**2 +
        phi.y**2 +
        phi.z**2
    )


def within_surf**e(
    phi,
    radius=100.0
):

**  return sovereignty_distance(phi**<= radius