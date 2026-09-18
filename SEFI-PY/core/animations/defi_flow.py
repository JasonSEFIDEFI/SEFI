from manim import *

class DEFILayerFlow(Scene):
    def construct(self):
        title = Text("DEFI: Entity Flow", font_size=40).to_edge(UP)

        centers = [LEFT*3, RIGHT*3, UP*2, DOWN*2, ORIGIN]
        nodes = VGroup(*[Circle(radius=0.3, color=BLUE).shift(c) for c in centers])

        edges = VGroup()
        for i, a in enumerate(nodes):
            for j, b in enumerate(nodes):
                if i < j:
                    edges.add(Line(a.get_center(), b.get_center(), color=GRAY, stroke_opacity=0.3))

        flows = edges.copy().set_color(YELLOW).set_stroke(opacity=0.0)

        self.play(FadeIn(title))
        self.play(FadeIn(nodes))
        self.play(FadeIn(edges))

        self.play(flows.animate.set_stroke(opacity=0.8), run_time=2)

        for e in flows:
            self.play(e.animate.set_color(TEAL), run_time=0.2)

        self.wait(2)
