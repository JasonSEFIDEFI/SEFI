from manim import *

class SEFIUnifiedOutro(Scene):
    def construct(self):
        title = Text("SEFI-PY Film Complete", font_size=48)
        subtitle = Text("GWFM • SEFI • Photonics • DEFI", font_size=32)
        subtitle.next_to(title, DOWN)

        self.play(FadeIn(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
