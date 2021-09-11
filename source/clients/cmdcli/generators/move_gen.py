from cmdcli.generators.generator import Generator
from cmdcli.generators.sanitize_functs import *

class MoveGen(Generator):
    """
    Generator for move command.
    """
    def __init__(self):
        self.key = "m"
        super().__init__()

    def create_command(self, split):
        """
        Create move command.
        """
        origin = str2coor(split[0])
        dest = str2coor(split[1])
        # create command
        cmd = {"command" : "MOVE",
               "origin"  : origin,
               "dest"    : dest}    
        return cmd
