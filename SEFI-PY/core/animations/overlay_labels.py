from manim import *

class OverlayLabels(Scene):
    def construct(self):
        labels = VGroup(
            Text("GWFM: Geometric Worldline Field Model", font_size=28).to_edge(UP),
            Text("SEFI: Single Entity Field Interpretation", font_size=28).to_edge(UP),
            Text("SEFI Photonics: Encoding & Channels", font_size=28).to_edge(UP),
            Text("DEFI: Distributed Entity Field Interpretation", font_size=28).to_edge(UP),
        )
        for lbl in labels:
            self.play(FadeIn(lbl))
            self.wait(1)
            self.play(FadeOut(lbl))
