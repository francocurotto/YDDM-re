from commandline.generators.roll_gen    import RollGen
from commandline.generators.dim_gen     import DimGen
from commandline.generators.skip_gen    import SkipGen
from commandline.generators.move_gen    import MoveGen
from commandline.generators.attack_gen  import AttackGen
from commandline.generators.wait_gen    import WaitGen
from commandline.generators.guard_gen   import GuardGen
from commandline.generators.endturn_gen import EndturnGen
from commandline.generators.quit_gen    import QuitGen
from commandline.generators.sanitize_functs import *
from duel.roll_state import DuplicatedDice

class CmdGenerator():
    """
    Generates a valid yddm-re command from text.
    """
    def __init__(self):
        rollgen    = RollGen()
        dimgen     = DimGen()
        skipgen    = SkipGen()
        movegen    = MoveGen()
        attackgen  = AttackGen()
        waitgen    = WaitGen()
        guardgen   = GuardGen()
        endturngen = EndturnGen()
        quitgen    = QuitGen()
        self.generators = [rollgen, dimgen, skipgen, movegen,
        attackgen, waitgen, guardgen, endturngen, quitgen]
        self.cmderrors = (IndexValueError, OOBIndexError,
            CoordinatesError, OOBCoordinatesError, 
            NetValueError, TransValueError, 
            DuplicatedDice)

    def create_command(self, split):
        """
        Creates command from splited text. If command is
        invalid, raise InvalidTextCommand.
        """
        try:
            for gen in self.generators:
                if gen.key == split[0]:
                    return gen.create_command(split[1:])
            # no generator found
            errortext = "No command with key " + split[0]
            raise InvalidTextCommand(errortext)
        except self.cmderrors as e:
            raise InvalidTextCommand(e.message)

    def list_commands(self):
        """
        Create a list of descriptions of all commands.
        """
        strlist = [gen.desc for gen in self.generators]
        return strlist
            
class InvalidTextCommand(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self, self.message)
