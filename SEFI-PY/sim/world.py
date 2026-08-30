class World:
    def __init__(self, global_field, boundary_radius, ambient_intensity):
        self.entities = []
        self.environment = Environment(
            global_field=global_field,
            boundary_radius=boundary_radius,
            ambient_intensity=ambient_intensity
        )
