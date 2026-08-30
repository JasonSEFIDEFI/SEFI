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
