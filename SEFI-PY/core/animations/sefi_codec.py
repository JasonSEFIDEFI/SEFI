from manim import *
import numpy as np

class SEFIPhotonCodec(Scene):
    def construct(self):
        title = Text("SEFI Photonic Codec", font_size=40).to_edge(UP)

        geom = Circle(radius=1.5, color=BLUE)
        phase_bar = NumberLine(x_range=[0, TAU], length=6).shift(DOWN*2)
        phase_dot = Dot(color=YELLOW).move_to(phase_bar.n2p(0))

        channel = Line(LEFT*3, RIGHT*3, color=YELLOW).shift(DOWN*0.5)
        decoded = Circle(radius=1.5, color=GREEN).shift(RIGHT*4)

        self.play(FadeIn(title))
        self.play(Create(geom))
        self.play(FadeIn(phase_bar), FadeIn(phase_dot))
        self.play(FadeIn(channel), FadeIn(decoded))

        for angle in [0, PI/2, PI, 3*PI/2, TAU]:
            self.play(phase_dot.animate.move_to(phase_bar.n2p(angle)), run_time=0.8)
            self.play(geom.animate.set_color(YELLOW if angle < PI else RED), run_time=0.5)
            self.play(decoded.animate.set_color(GREEN if angle < PI else TEAL), run_time=0.5)

        self.wait(2)
