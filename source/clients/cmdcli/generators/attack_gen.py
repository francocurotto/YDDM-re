from cmdcli.generators.sanitize_functs import *

class AttackGen():
    """
    Generator for move command.
    """
    def __init__(self):
        self.key = "a"
        self.desc = desc

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

desc = "\
- ATTACK COMMAND: a XY1 XY2\n\
    - a XY1 XY2: make monster at position XY1 attack target\n\
        at position XY2."
