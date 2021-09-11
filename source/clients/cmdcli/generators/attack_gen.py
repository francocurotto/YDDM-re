from cmdcli.generators.generator import Generator
from cmdcli.generators.sanitize_functs import *

class AttackGen(Generator):
    """
    Generator for move command.
    """
    def __init__(self):
        self.key = "a"
        super().__init__()

    def create_command(self, split):
        """
        Create attack command.
        """
        origin = str2coor(split[0])
        dest = str2coor(split[1])
        # create command
        cmd = {"command" : "ATTACK",
               "origin"  : origin,
               "dest"    : dest}    
        return cmd
