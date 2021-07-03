from print_gen import PrintGen
from quit_gen import QuitGen

class HumanPlayer():
    """
    Player controled by human.
    """
    def __init__(self, name, icons):
        self.name = name
        # list of command generators
        printgen = PrintGen(icons)
        quitgen  = QuitGen()
        self.generators = [printgen, quitgen]

    def get_command(self, engine):
        """
        Generate the proper command given the user input. If
        not command should be generated (e.g. for print 
        commands) return None.
        """
        # read command from user input
        string = input(">> ")
        split = string.split()

        # print command list
        if split[0] == "l":
            strlist = []
            for gen in self.generators:
                strlist.append(gen.desc)
            print("\n\n".join(strlist))
            return None

        # excecute the correct generator
        for gen in self.generators:
            if gen.key == split[0]:
                return gen.create_command(engine, split[1:])

        # no generator found
        print("No command with key " + split[0])
        return None
