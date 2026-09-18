import numpy as np

def render_ascii_projection(voxel_grid: np.ndarray):
    """
    Generates a 2D ASCII projection of the voxel grid density along the Z-axis.
    """
    projection = np.sum(voxel_grid, axis=2)
    chars = [" ", ".", ":", "*", "o", "O", "#", "@"]
    max_val = np.max(projection) if np.max(projection) > 0 else 1.0
    
    ascii_frame = []
    for row in projection:
        line = "".join([chars[int((val / max_val) * (len(chars) - 1))] for val in row])
        ascii_frame.append(line)
    return "\n".join(ascii_frame)