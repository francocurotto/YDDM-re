from cmdcli.generators.sanitize_functs import *

class MoveGen():
    """
    Generator for move command.
    """
    def __init__(self):
        self.key = "m"
        self.desc = desc

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

desc = "\
- MOVE COMMAND: m XY1 XY2\n\
    - m XY1 XY2: move monster at position XY1 to position\n\
        XY2."
