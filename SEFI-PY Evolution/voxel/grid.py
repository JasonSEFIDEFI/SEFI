import numpy as np

class VoxelGrid:
    """
    Discretizes 3D/4D space into a voxel grid representation.
    """
    def __init__(self, bounds=(-5.0, 5.0), resolution=20):
        self.resolution = resolution
        self.grid = np.zeros((resolution, resolution, resolution), dtype=float)
        self.bounds = bounds
        self.lin = np.linspace(bounds[0], bounds[1], resolution)

    def map_point_to_index(self, point: np.ndarray):
        indices = np.digitize(point, self.lin) - 1
        return np.clip(indices, 0, self.resolution - 1)

    def add_trajectory(self, trajectory: np.ndarray, weight: float = 1.0):
        for pt in trajectory:
            idx = self.map_point_to_index(pt[:3])
            self.grid[tuple(idx)] += weight