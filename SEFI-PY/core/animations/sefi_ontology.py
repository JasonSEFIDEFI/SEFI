from manim import *
import numpy as np


class SEFIOntologyJourney(Scene):
    def construct(self):
        title = Text("SEFI Ontology", font_size=42).to_edge(UP)
        subtitle = Text(
            "one entity, five interpretable layers", font_size=22, color=GRAY_B
        ).next_to(title, DOWN, buff=0.12)

        self.play(FadeIn(title), FadeIn(subtitle))

        origin = Dot(ORIGIN, radius=0.12, color=YELLOW)
        origin_label = Text("FIELD ORIGIN", font_size=30, color=YELLOW)
        origin_label.next_to(origin, DOWN, buff=0.3)
        momentum = Arrow(
            origin.get_center(), origin.get_center() + RIGHT * 1.8 + UP * 0.7,
            buff=0, color=YELLOW, stroke_width=6,
        )
        momentum_label = Text("position + momentum", font_size=20, color=YELLOW)
        momentum_label.next_to(momentum, UP, buff=0.15)

        self.play(FadeIn(origin), Write(origin_label), GrowArrow(momentum))
        self.play(FadeIn(momentum_label))
        self.wait(0.5)

        authored_arrow = Arrow(
            origin.get_center(), origin.get_center() + RIGHT * 2.5 + UP * 1.3,
            buff=0, color=BLUE, stroke_width=7,
        )
        authored_label = Text("FIELD AUTHORSHIP", font_size=30, color=BLUE)
        authored_label.next_to(authored_arrow.get_end(), RIGHT, buff=0.2)
        authored_note = Text("identity becomes expressible", font_size=20, color=BLUE)
        authored_note.next_to(authored_label, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(
            ReplacementTransform(momentum, authored_arrow),
            ReplacementTransform(momentum_label, authored_note),
            ReplacementTransform(origin_label, authored_label),
            run_time=1.8,
        )
        self.wait(0.5)

        sovereignty = Circle(radius=1.0, color=GREEN, stroke_width=7)
        sovereignty.move_to(authored_arrow.get_end())
        sovereignty_label = Text("FIELD SOVEREIGNTY", font_size=30, color=GREEN)
        sovereignty_label.next_to(sovereignty, DOWN, buff=0.3)
        sovereignty_note = Text("persistence + self-governance", font_size=20, color=GREEN)
        sovereignty_note.next_to(sovereignty_label, DOWN, buff=0.1)

        self.play(
            Create(sovereignty),
            ReplacementTransform(authored_label, sovereignty_label),
            ReplacementTransform(authored_note, sovereignty_note),
            run_time=1.5,
        )
        self.wait(0.5)

        expression = ParametricFunction(
            lambda t: np.array([
                1.9 * np.cos(t),
                0.75 * np.sin(2 * t),
                0,
            ]) + sovereignty.get_center(),
            t_range=[0, TAU],
            color=TEAL,
            stroke_width=6,
        )
        expression_label = Text("WARP:EXPRESSION", font_size=30, color=TEAL)
        expression_label.next_to(expression, RIGHT, buff=0.2)
        expression_note = Text("the sovereign field moves", font_size=20, color=TEAL)
        expression_note.next_to(expression_label, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(
            ReplacementTransform(sovereignty, expression),
            ReplacementTransform(sovereignty_label, expression_label),
            ReplacementTransform(sovereignty_note, expression_note),
            run_time=1.8,
        )
        self.wait(0.5)

        defi_nodes = VGroup(
            *[
                Dot(
                    expression.get_center()
                    + RIGHT * 2.3 * np.cos(angle)
                    + UP * 1.1 * np.sin(angle),
                    radius=0.1,
                    color=ORANGE,
                )
                for angle in np.linspace(0, TAU, 5, endpoint=False)
            ]
        )
        defi_edges = VGroup(
            *[
                Line(expression.get_center(), node.get_center(), color=ORANGE, stroke_width=3)
                for node in defi_nodes
            ]
        )
        defi_label = Text("WARP:DEFI", font_size=30, color=ORANGE)
        defi_label.next_to(defi_nodes, RIGHT, buff=0.2)
        defi_note = Text("active field integration", font_size=20, color=ORANGE)
        defi_note.next_to(defi_label, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(
            Create(defi_edges),
            FadeIn(defi_nodes),
            ReplacementTransform(expression_label, defi_label),
            ReplacementTransform(expression_note, defi_note),
            run_time=1.8,
        )
        self.play(
            LaggedStart(
                *[node.animate.scale(1.35).set_color(YELLOW) for node in defi_nodes],
                lag_ratio=0.12,
            ),
            run_time=1.4,
        )
        self.wait(2)