# sim/sim_engine.py

from sim.entity import Entity
from sim.world import World

def run_sim(steps=10, dt=0.1):
    world = World()

    # one entity for now
    e = Entity([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    world.add(e)

    print("\n--- SEFI-SIM ---")

    for i in range(steps):
        world.step(dt)
        print(f"Step {i+1}: Momentum = {e.origin.momentum}")
def run_sim(steps=10, dt=0.1):
    world = World()

    e1 = Entity([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    e2 = Entity([2.0, -1.0, 0.0], [-0.5, 0.5, 0.0])

    world.add(e1)
    world.add(e2)

    print("\n--- SEFI-SIM ---")

    for i in range(steps):
        world.step(dt)
        print(f"Step {i+1}:")
        print(f"  E1 Pos = {e1.origin.position}, Mom = {e1.origin.momentum}")
        print(f"  E2 Pos = {e2.origin.position}, Mom = {e2.origin.momentum}")
drive = compute_drive(e1)
orient = compute_orientation(e1)
print(f"  E1 Drive = {drive}, Orient = {orient}")
world = World()
# add entities
for i in range(steps):
    world.step(dt)
    ...
from config import SIM_CONFIG, ENTITY_CONFIGS
from sim.world import World
from sim.dna import EntityDNA
from sim.entity import Entity

def run_sim():
    world = World(
        global_field=SIM_CONFIG["global_field"],
        boundary_radius=SIM_CONFIG["boundary_radius"],
        ambient_intensity=SIM_CONFIG["ambient_intensity"]
    )

    for cfg in ENTITY_CONFIGS:
        dna = EntityDNA(
            position=cfg["position"],
            momentum=cfg["momentum"],
            sovereignty_bias=cfg["sovereignty_bias"],
            expression_bias=cfg["expression_bias"],
            defi_bias=cfg["defi_bias"]
        )
        world.add(Entity(dna))

    for i in range(SIM_CONFIG["steps"]):
        world.step(SIM_CONFIG["dt"])
        print(f"Step {i+1}:")
        for idx, e in enumerate(world.entities):
            print(f"  E{idx+1} Pos={e.origin.position}, Mom={e.origin.momentum}")
class World:
    def __init__(self, global_field, boundary_radius, ambient_intensity):
        self.entities = []
        self.environment = Environment(
            global_field=global_field,
            boundary_radius=boundary_radius,
            ambient_intensity=ambient_intensity
        )
