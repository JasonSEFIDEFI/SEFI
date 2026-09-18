from manim import *
import numpy as np

from manim import *
import numpy as np

class WorldlineCurvature(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
        )

        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)
        self.add(axes)

        t = np.linspace(0, 6, 400)
        x = np.cos(t)
        y = np.sin(t)
        z = 0.2 * t

        worldline = VMobject()
        worldline.set_points_smoothly([np.array([x[i], y[i], z[i]]) for i in range(len(t))])
        worldline.set_color(YELLOW)

        self.play(Create(worldline), run_time=4)
        self.wait()
