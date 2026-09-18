from manim import *

class FadeTransition(Scene):
    def construct(self):
        rect = Rectangle(width=14, height=8, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(rect, run_time=1))
        self.play(FadeOut(rect, run_time=1))
