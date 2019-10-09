"""Unit tests for simulation.py."""
import unittest
from simulation import Simulation
from virus import Virus
from person import Person


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

    # test 2
    sim2 = Simulation(30, 1, 0)
    assert len(sim2.population) == 30

    vaccinated_count = 0
    for person in sim2.population:
        if person.is_vaccinated:
            vaccinated_count += 1
    assert vaccinated_count == 30

    infected_count = 0
    for person in sim2.population:
        if person.infection is not None:
            infected_count += 1
    assert infected_count == 0

    rest_count = 0
    for person in sim2.population:
        if not person.is_vaccinated and person.infection is None:
            rest_count += 1
    assert rest_count == 0

    # no duplicate IDs
    id_nums_list = []
    for person in sim2.population:
        assert person._id not in id_nums_list
        id_nums_list.append(person._id)


def test_sim_should_continue():
    """Test that the simulaion ends properly."""
    sim = Simulation(30, 1, 0)
    assert not sim._simulation_should_continue()

    sim2 = Simulation(30, 0, 30)
    assert sim2._simulation_should_continue()

    sim3 = Simulation(30, .5, 5)
    assert sim3._simulation_should_continue()

    sim4 = Simulation(0, 0, 0)
    person1 = Person(1, False)
    person2 = Person(2, False)
    person3 = Person(3, False)
    person4 = Person(4, False)
    sim4.population = [person1, person2, person3, person4]
    assert sim4._simulation_should_continue()
    person2.is_alive = False
    person3.is_alive = False
    assert sim4._simulation_should_continue()
    person1.is_alive = False
    person4.is_alive = False
    assert not sim4._simulation_should_continue()


def test_run():
    """Test that the sim runs without error."""
    sim = Simulation(30, 1, 0)
    sim.run()
    sim = Simulation(0, 1, 0)
    sim.run()
