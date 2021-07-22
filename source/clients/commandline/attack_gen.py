from sanitize_functs import *

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
        # check argument number
        if len(split)!=2:
            print("Number of arguments must be 2")
            return
        # sanitize pos
        origin = str2coor(split[0])
        if not origin:
            return None
        # sanitize pos
        dest = str2coor(split[1])
        if not dest:
            return None

        # create command
        cmd = {"command" : "ATTACK",
               "origin"  : origin,
               "dest"    : dest}    
        return cmd

desc = "\
- ATTACK COMMAND: a XY1 XY2\n\
    - m XY1 XY2: make monster at position XY1 attack target\n\
        at position XY2."
