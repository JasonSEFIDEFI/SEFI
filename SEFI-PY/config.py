# config.py

SIM_CONFIG = {
    "steps": 50,
    "dt": 0.1,
    "global_field": [0.0, 1.0, 0.0],
    "boundary_radius": 10.0,
    "ambient_intensity": 0.05
}

ENTITY_CONFIGS = [
    {
        "position": [0.0, 1.0, 0.0],
        "momentum": [1.0, 0.0, 0.0],
        "sovereignty_bias": 1.2,
        "expression_bias": 1.0,
        "defi_bias": 1.0
    },
    {
        "position": [2.0, -1.0, 0.0],
        "momentum": [-0.5, 0.5, 0.0],
        "sovereignty_bias": 0.8,
        "expression_bias": 1.3,
        "defi_bias": 1.1
    }
]
