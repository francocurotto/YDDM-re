from sanitize_functs import *
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
        # check argument number
        if len(split)<3:
            print("Number of arguments must be 3 or greater")
            return
        # sanitize dice integer
        i = str2index(split[0], 0, 2)
        if i is None:
            return None
        # sanitize net
        net = str2net(split[1])
        if not net:
            return None
        # sanitize pos
        pos = str2coor(split[2])
        if not pos:
            return None
        # sanitize transformations
        translist = []
        for string in split[3:]:
            trans = str2trans(string)
            if not trans:
                return None
            translist.append(trans)

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
