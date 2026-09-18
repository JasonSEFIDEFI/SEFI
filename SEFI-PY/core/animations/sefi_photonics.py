from manim import *
import numpy as np

class SEFIPhotonics(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70*DEGREES, theta=40*DEGREES)

        ring = Circle(radius=2, color=BLUE).rotate(PI/2, axis=RIGHT)
        label = Text("SEFI Photonics: SPDC & Encoding", font_size=36).to_edge(UP)

        photons = VGroup()
        for a in np.linspace(0, TAU, 20):
            p = Dot3D(point=[2*np.cos(a), 2*np.sin(a), 0], color=YELLOW)
            photons.add(p)

        rays = VGroup()
        for p in photons:
            r = Line3D(p.get_center(), p.get_center()+np.array([0,0,3]), color=YELLOW)
            rays.add(r)

        self.play(FadeIn(label))
        self.play(Create(ring))
        self.play(FadeIn(photons))
        self.play(Create(rays), run_time=3)

        self.play(photons.animate.set_color(RED), run_time=2)
        self.wait(2)
