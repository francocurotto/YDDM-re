import readline # for input history
from print_gen   import PrintGen
from roll_gen    import RollGen
from dim_gen     import DimGen
from skip_gen    import SkipGen
from move_gen    import MoveGen
from attack_gen  import AttackGen
from endturn_gen import EndturnGen
from quit_gen    import QuitGen
from sanitize_functs import IndexValueError
from sanitize_functs import IndexUnboundError
from sanitize_functs import CoordinatesError
from sanitize_functs import CoordinatesUnboundError
from sanitize_functs import NetValueError
from sanitize_functs import TransValueError
from duel.roll_state import DiceDuplicatedError

class HumanPlayer():
    """
    Player controled by human.
    """
    def __init__(self, engine, name, stringifier):
        self.name = name
        # list of command generators
        printgen   = PrintGen(engine, stringifier)
        rollgen    = RollGen()
        dimgen     = DimGen()
        skipgen    = SkipGen()
        movegen    = MoveGen()
        attackgen  = AttackGen()
        endturngen = EndturnGen()
        quitgen    = QuitGen()
        self.generators = [printgen, rollgen, dimgen, 
            skipgen, movegen, attackgen, endturngen, quitgen]
        self.cmderrors = (IndexValueError, IndexUnboundError,
            CoordinatesError, CoordinatesUnboundError, 
            NetValueError, TransValueError, 
            DiceDuplicatedError)

    def get_command(self):
        """
        Generate the proper command given the user input. If
        not command should be generated (e.g. for print 
        commands) return None.
        """
        # read command from user input
        string = input(">> ")
        split = string.split()

        try:
            # print command list
            if split[0] == "l":
                self.print_cmd_list(self)
                return None

            # excecute the correct generator
            for gen in self.generators:
                if gen.key == split[0]:
                    return gen.create_command(split[1:])

            # no generator found
            print("No command with key " + split[0])
            return None

        except IndexError:
            print("Not enough arguments")
            return None

        except self.cmderrors as e:
            # print error while generating command
            print(e.message)
            return None

    def print_cmd_list(self):
        """
        Print commands list and descriptions.
        """
        strlist = []
        for gen in self.generators:
            strlist.append(gen.desc)
        print("\n\n".join(strlist))
