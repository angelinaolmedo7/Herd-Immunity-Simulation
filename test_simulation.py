"""Unit tests for simulation.py."""
import unittest
from simulation import Simulation
from virus import Virus


def test_pop_creation():
    """Test that the population is being created correctly."""
    sim = Simulation(1000, .1, 50, Virus('test', .5, .5))
    assert len(sim.population) == 1000

    vaccinated_count = 0
    for person in sim.population:
        if person.is_vaccinated:
            vaccinated_count += 1
    assert vaccinated_count == 100

    infected_count = 0
    for person in sim.population:
        if person.infection is not None:
            infected_count += 1
    assert infected_count == 50

    rest_count = 0
    for person in sim.population:
        if not person.is_vaccinated and person.infection is None:
            rest_count += 1
    assert rest_count == 850

    # no duplicate IDs
    id_nums_list = []
    for person in sim.population:
        assert person._id not in id_nums_list
        id_nums_list.append(person._id)
