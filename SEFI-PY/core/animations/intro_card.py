from manim import *

class SEFIUnifiedIntro(Scene):
    def construct(self):
        title = Text("GWFM • SEFI • Photonics • DEFI", font_size=64)
        subtitle = Text("Unified Entity Field Film", font_size=36)
        subtitle.next_to(title, DOWN)

        self.play(FadeIn(title, shift=UP))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
