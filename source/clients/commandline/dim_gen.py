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
        if len(split)!=1:
            print("Number of arguments must be 1")
            return
        # sanitize arguments
        try:
            i = int(split[0])-1
        except ValueError:
            print("Cannot convert integer")
            return None
        try:
            dice = engine.dsm.state.dimdice[i-1]
        except IndexError;
            print("Integer out of candidates bound")
            return None
        # get net
        while True:
            net_string = stringifier.stringify_nets(dice)
            print(net_string)
            string = input("Select net: (c:cancel)")
            if string == "c":
                return None
            if reply in engine.NETS:
                break
        # get pos and trans
        string = input("Input net position XY (c:cancel)")

        # create command
        cmd = {"command" : "ROLL", "dice" : dice}
        return cmd

desc = "\
- DIM COMMAND [DIM state]: d D\n\
    - d D: dimension dice D from summon candidates"
