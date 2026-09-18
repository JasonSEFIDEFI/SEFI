from manim import *
import numpy as np

class SEFICore(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60*DEGREES, theta=25*DEGREES)
        self.add(axes)

        field = Surface(
            lambda u, v: np.array([
                u,
                v,
                0.3*np.sin(u*2) * np.cos(v*2)
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=30,
            fill_color=PURPLE,
            fill_opacity=0.5,
        )

        label = Text("SEFI: Sovereignty-Preserving Field", font_size=36).to_edge(UP)

        self.play(FadeIn(label))
        self.play(FadeIn(field))
        self.play(field.animate.scale(1.2), run_time=2)
        self.play(field.animate.rotate(PI/4), run_time=2)
        self.wait(2)
