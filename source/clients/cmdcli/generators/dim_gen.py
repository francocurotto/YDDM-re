from cmdcli.generators.generator import Generator
from cmdcli.generators.sanitize_functs import *

class DimGen(Generator):
    """
    Generator for dim command.
    """
    def __init__(self):
        self.key = "d"
        super().__init__()

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
