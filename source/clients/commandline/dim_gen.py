class DimGen():
    """
    Generator for dim command.
    """
    def __init__(self):
        self.key = "d"
        self.desc = desc

    def create_command(self, engine, split):
        """
        Create a dim command.
        """
        # check argument number
        if len(split)<3:
            print("Number of arguments must be 3 or greater")
            return
        # sanitize dice integer
        try:
            i = int(split[0])
        except ValueError:
            print("Cannot convert integer")
            return None
        try:
            dice = engine.dsm.state.dimdice[i-1]
        except IndexError;
            print("Integer out of candidates bound")
            return None
        # get net
        net = split[1]
        if net not in engine.NETS:
            print("Invalid net name")
            return None
        # get pos
        

desc = "\
- DIM COMMAND [DIM state]: d D N XY [T1, T2,...]\n\
    - d D N XY [T1 T2 ...]: dimension dice D from candidates,
        using net N, at position XY, and optionally apply
        transformations T1, T2, ... to net before dimension."
