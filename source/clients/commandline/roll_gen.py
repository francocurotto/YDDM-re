class RollGen():
    """
    Generator for roll command.
    """
    def __init__(self):
        self.key = "r"
        self.desc = desc

    def create_command(self, engine, split):
        """
        Create a roll command.
        """
        # check argument number
        if len(split)!=3:
            print("Number of arguments must be 3")
            return
        # sanitize arguments
        try:
            dice = [int(i)-1 for i in split]
        except ValueError:
            print("Cannot convert integer")
            return
        for i in dice:
            if i<0 or i>14:
                print("Integer out of pool bound")
                return
        # create command
        cmd = {"command" : "ROLL", "dice" : dice}
        return cmd

desc = "\
- ROLL COMMAND: r D1 D2 D3\n\
    - r D1 D2 D3: roll dice D1, D2 and D3 from dice pool."
