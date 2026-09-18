class DEFILayer(Scene):
    def construct(self):
        # network graph: circles (nodes) connected by lines
        # animate flows along edges
        # keep a ghosted background of the SEFI field to show origin
        ...
from manim import *

class DEFILayer(Scene):
    def construct(self):
        label = Text("DEFI: Distributed Entity Field Interpretation", font_size=36).to_edge(UP)

        nodes = VGroup(
            *[Circle(radius=0.3, color=BLUE).shift(v) for v in
              [LEFT*3, RIGHT*3, UP*2, DOWN*2, ORIGIN]]
        )

        edges = VGroup()
        for a in nodes:
            for b in nodes:
                if a != b:
                    edges.add(Line(a.get_center(), b.get_center(), color=GRAY, stroke_opacity=0.3))

        flows = edges.copy().set_color(YELLOW)

        self.play(FadeIn(label))
        self.play(FadeIn(nodes))
        self.play(FadeIn(edges))
        self.play(flows.animate.set_stroke(opacity=0.8), run_time=3)
        self.wait(2)
