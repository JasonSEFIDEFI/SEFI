"""
pauli_ops.py
------------
Real Pauli operations for SEFI-QEC.

State vectors:
    |0> = [1, 0]
    |1> = [0, 1]
"""

def pauli_x(state):
    # Flip |0> <-> |1>
    return [state[1], state[0]]

def pauli_z(state):
    # Phase flip: |0> -> |0>, |1> -> -|1>
    return [state[0], -state[1]]

def pauli_y(state):
    # Y = iXZ (phase ignored for classical simulation)
    flipped = pauli_x(state)
    return pauli_z(flipped)
