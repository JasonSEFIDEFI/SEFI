from manim import *
import numpy as np

class SEFISovereigntyMorph(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=30*DEGREES)

        axes = ThreeDAxes()
        self.add(axes)

        # Worldline
        t = np.linspace(0, 6, 400)
        pts = [np.array([np.cos(v), np.sin(v), 0.2*v]) for v in t]
        worldline = VMobject(color=YELLOW)
        worldline.set_points_smoothly(pts)

        # Field
        field = Surface(
            lambda u, v: np.array([
                u,
                v,
                0.3*np.sin(u*2) * np.cos(v*2)
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=12,
            fill_color=PURPLE,
            fill_opacity=0.5,
        )

        label = Text("SEFI: Sovereignty Morph", font_size=36).to_edge(UP)

        self.play(FadeIn(label))
        self.play(Create(worldline), run_time=3)
        self.wait(1)
        self.play(ReplacementTransform(worldline, field), run_time=3)
        self.play(field.animate.scale(1.2), run_time=2)
        self.wait(2)
