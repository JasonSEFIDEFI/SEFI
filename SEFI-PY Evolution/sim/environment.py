import numpy as np

class SimulationEnvironment:
    """
    Defines external field perturbation conditions.
    """
    def __init__(self, noise_level: float = 0.005):
        self.noise_level = noise_level

    def apply_field_noise(self, position: np.ndarray) -> np.ndarray:
        return position + np.random.normal(0.0, self.noise_level, size=position.shape)