from cmdcli.generators.sanitize_functs import *

class DimGen():
    """
    Generator for dim command.
    """
    def __init__(self):
        self.key = "d"
        self.desc = desc

    def create_command(self, split):
        """
        Create a dim command.
        """
        i = str2index(split[0], 0, 2)
        net = str2net(split[1])
        pos = str2coor(split[2])
        translist = [str2trans(s) for s in split[3:]]
        # create command
        cmd = {"command" : "DIM",
               "dice"    : i,
               "net"     : net,
               "pos"     : pos,
               "trans"   : translist}    
        return cmd

desc = "\
- DIM COMMAND: d D N XY [T1, T2,...]\n\
    - d D N XY [T1 T2 ...]: dimension dice D from\n\
        candidates, using net N, at position XY, and\n\
        optionally apply transformations T1, T2, ... to net\n\
        before dimension."
