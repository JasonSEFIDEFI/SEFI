import pytest
import numpy as np

from sim.world import World
from sim.entity import Entity


def test_world_initialization():
    world = World(
        global_field=[0.0, 0.0, 1.0],
        boundary_radius=10.0,
        ambient_intensity=0.2
    )

    assert world.entities == []
    assert world.environment.global_field == [0.0, 0.0, 1.0]
    assert world.environment.boundary_radius == 10.0
    assert world.environment.ambient_intensity == 0.2


def test_world_add_entity():
    world = World()
    e = Entity([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])

    world.add(e)

    assert len(world.entities) == 1
    assert world.entities[0] is e


def test_world_step_updates_entity():
    world = World(
        global_field=[0.0, 0.0, 1.0],
        boundary_radius=10.0,
        ambient_intensity=0.1
    )

    e = Entity([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    world.add(e)

    # capture initial state
    initial_pos = np.array(e.origin.position)
    initial_mom = np.array(e.origin.momentum)

    # step world
    world.step(dt=0.1)

    # new state
    new_pos = np.array(e.origin.position)
    new_mom = np.array(e.origin.momentum)

    # momentum should change due to:
    # - behavior layer
    # - DEFI evolution
    # - global field
    assert not np.allclose(initial_mom, new_mom)

    # position should change due to momentum evolution
    assert not np.allclose(initial_pos, new_pos)


def test_world_boundary_pushes_entity_back():
    # boundary radius is small so entity starts outside
    world = World(
        global_field=[0.0, 0.0, 0.0],
        boundary_radius=1.0,
        ambient_intensity=0.0
    )

    # place entity far outside boundary
    e = Entity([5.0, 0.0, 0.0], [0.0, 0.0, 0.0])
    world.add(e)

    world.step(dt=0.1)

    # momentum should now point back toward origin
    mx, my, mz = e.origin.momentum
    assert mx < 0  # pushed left toward origin


def test_sefi_layers_rebuild_each_step():
    world = World()
    e = Entity([0.0, 1.0, 0.0], [1.0, 0.0, 0.0])
    world.add(e)

    # capture old objects
    old_auth = e.authorship
    old_sov = e.sovereignty
    old_exp = e.expression
    old_defi = e.defi

    world.step(dt=0.1)

    # layers must be rebuilt (new object instances)
    assert e.authorship is not old_auth
    assert e.sovereignty is not old_sov
    assert e.expression is not old_exp
    assert e.defi is not old_defi
