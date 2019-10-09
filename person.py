"""People in the simulation that can get infected and die."""
from virus import Virus
# import unittest
import random
random.seed(42)


class Person(object):
    """Person objects will populate the simulation."""

    def __init__(self, _id, is_vaccinated, infection=None):
        """
        Start with is_alive = True, because we don't make vampires or zombies.

        All other values will be set by the simulation when it makes each
        Person object.

        If person is chosen to be infected when the population is created, the
        simulation should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        """
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # Virus object or None

    def test_cases(self):
        """Tests for person."""
        test_vacc_person_instantiation()
        test_not_vacc_person_instantiation()
        test_sick_person_instantiation()
        test_did_survive_infection()

    def did_survive_infection(self):
        """Generate a random number and compare to virus's mortality_rate.

        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        """
        # Only called if infection attribute is not None.
        # Should return a Boolean
        if self.infection is None:  # just in case
            pass
        roll = random.random()
        # print(roll)
        # print(self.infection.mortality_rate)
        survived = roll >= self.infection.mortality_rate
        if survived:  # remove infection and vaccinate
            self.infection = None
            self.is_vaccinated = True
        else:  # kill
            self.is_alive = False
        return survived


# Simple tests to ensure Person class is instantiated correctly.
def test_vacc_person_instantiation():
    """Create person to test if our init method works as expected."""
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    """Create person to test if our init method works as expected."""
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None


def test_sick_person_instantiation():
    """Create person to test if our init method works as expected."""
    # Create a Virus object to give a Person object an infection
    virus = Virus('Dysentery', 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is not None
    assert person.infection.name in 'Dysentery'
    assert person.infection.repro_rate == 0.7
    assert person.infection.mortality_rate == 0.2


def test_did_survive_infection():
    """Test did_survive_infection() kills/vaccinates properly."""
    # Create a Virus object to give a Person object an infection
    virus = Virus('Dysentery', 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        assert person.is_vaccinated is True
        assert person.infection is None
    else:
        assert person.is_alive is False
        assert person.infection.name in 'Dysentery'


person = Person(0, True)
person.test_cases()
