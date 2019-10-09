"""Log activity during sim."""


class Logger(object):
    """Utility class for logging all interactions during the simulation.

    Params:
        file_name: name of file to store metadata
    """

    # TODO: Write a test suite for this class to make sure each method is
    # working as expected.

    def test_cases(self):
        """Assert all test cases here."""
        # PROTIP: Write your tests before you solve each function, that way you
        # can test them one by one as you write your class.
        self.write_metadata(100000, 0.90, "Ebola", 0.70, 0.35)
        self.log_interaction("Ryan", "rando", False, False, False)
        return

    def __init__(self, file_name):
        """Initialize logger.

        The file_name passed should be the full file name of the file that the
        logs will be written to.
        self.file_name = file_name
        """
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name,
                       mortality_rate, basic_repro_num):
        """Log metadata immediately.

        The simulation class should use this method immediately to log the
        specific parameters of the simulation as the first line of the file.
        """
        # This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # Use 'w' mode when you open the file. For all other methods, use the
        # 'a' mode to append a new log to the end, 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure
        # that each event logged ends up on a separate line!

        # Creates a str of all user inputs, seperated by commas.
        metadata = f"{pop_size},{vacc_percentage},{virus_name},{mortality_rate},{basic_repro_num}"

        # writes metadata to a file named metadata
        data_file = open(self.file_name, "w")
        data_file.write(metadata)
        d

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.

        # Infect person if theyre not vaccinated
        if random_person_sick == False and not random_person_vacc:
            did_infect == True
            random_person_sick == True
            print(f"{random_person} got infected by {person}!")

        # If you try to infect a sick person:
        elif random_person_sick == True:
            print(
                f"{person} didn't infect {random_person} bacause they're already sick")
            did_infect == False
            random_person_sick == True

        # If you try to infect a vaccinated person:
        elif random_person_vacc == True:
            print(
                f"{person} didn't infect {random_person} because they're vaccinated ")
            did_infect == False
            random_person_sick == False

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # TODO: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        if did_die_from_infection == True:
            print(f"{person} died!")
        elif did_die_from_infection == False:
            print(f"{person} lived!")

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass


log = Logger('metadata')
log.test_cases()
