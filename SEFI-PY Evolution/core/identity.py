import numpy as np
from dataclasses import dataclass

@dataclass
class SEFIState:
    origin: float
    authorship: float
    sovereignty: float
    warp: float

    def to_vector(self) -> np.ndarray:
        return np.array([self.origin, self.authorship, self.sovereignty, self.warp])