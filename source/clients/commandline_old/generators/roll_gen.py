from sanitize_functs import *
from duel.roll_state import DuplicatedDice

class RollGen():
    """
    Generator for roll command.
    """
    def __init__(self):
        self.key = "r"
        self.desc = desc

    def create_command(self, split):
        """
        Create a roll command.
        """
        # get dice indeces
        indeces = []
        for string in [split[0],split[1],split[2]]:
            i = str2index(string, 0, 14)
            if i in indeces:
                raise DuplicatedDice
            indeces.append(i)
        # create command
        cmd = {"command" : "ROLL", "dice" : indeces}
        return cmd
                    
desc = "\
- ROLL COMMAND: r D1 D2 D3\n\
    - r D1 D2 D3: roll dice D1, D2 and D3 from dice pool"
