import random


def bit_flip(bits, p=0.05):
    """
    X error channel.
    """

    out = bits.copy()

    for i in range(len(out)):
        if random.random() < p:
            out[i] ^= 1

    return out


def phase_flip(bits, p=0.05):
    """
    Placeholder Z channel.

    Recorded as metadata until
    full state-vector simulation exists.
    """

    return bits.copy()


def depolarizing(bits, p=0.05):
    """
    Simple depolarizing channel.
    """

    out = bits.copy()

    for i in range(len(out)):
        if random.random() < p:
            out[i] = random.choice([0, 1])

    return out