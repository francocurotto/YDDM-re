from sanitize_functs import *

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
        cmd = {"command" : "MOVE",
               "origin"  : origin,
               "dest"    : dest}    
        return cmd

desc = "\
- MOVE COMMAND: m XY1 XY2\n\
    - d XY1 XY2: move monster at position XY1 to position\n\
        XY2."
