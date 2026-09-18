from manim import *
import numpy as np

class WarpExpressionBridge(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=30*DEGREES)

        field = Surface(
            lambda u, v: np.array([
                u,
                v,
                0.4*np.sin(u*2 + v*2)
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=40,
            fill_color=TEAL,
            fill_opacity=0.5,
        )

        label = Text("WARP: Expression Layer", font_size=36).to_edge(UP)

        self.play(FadeIn(label))
        self.play(FadeIn(field))
        self.play(field.animate.scale(1.3), run_time=2)
        self.play(field.animate.rotate(PI/3), run_time=2)
        self.wait(2)
