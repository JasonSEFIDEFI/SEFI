from manim import *
import numpy as np

class GWFMIntro(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)
        self.add(axes)

        t = np.linspace(0, 6, 400)
        points = [np.array([np.cos(value), np.sin(value), 0.2 * value]) for value in t]
        worldline = VMobject(color=YELLOW)
        worldline.set_points_smoothly(points)

        surface = Surface(
            lambda u, v: np.array([u, v, 0.2 * u]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=20,
            fill_opacity=0.2,
            fill_color=BLUE,
        )
        label = Text("GWFM: Worldline Geometry", font_size=36).to_edge(UP)

        self.play(FadeIn(label))
        self.play(Create(worldline), run_time=4)
        self.play(FadeIn(surface), run_time=2)
        self.wait(2)
