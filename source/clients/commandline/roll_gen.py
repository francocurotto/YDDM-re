from sanitize_functs import *

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
        # check argument number
        if len(split)!=3:
            print("Number of arguments must be 3")
            return
        # get dice indeces
        indeces = set()
        for string in split:
            i = str2index(string, 0 , 14)
            if i is None:
                return None
            # check for repetition
            if i in indeces:
                print("Cannot use the same dice twice")
                return None
            indeces.add(i)
        # create command
        cmd = {"command" : "ROLL", "dice" : indeces}
        return cmd

desc = "\
- ROLL COMMAND: r D1 D2 D3\n\
    - r D1 D2 D3: roll dice D1, D2 and D3 from dice pool"
