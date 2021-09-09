from cmdcli.generators.roll_gen    import RollGen
from cmdcli.generators.dim_gen     import DimGen
from cmdcli.generators.skip_gen    import SkipGen
from cmdcli.generators.move_gen    import MoveGen
from cmdcli.generators.attack_gen  import AttackGen
from cmdcli.generators.wait_gen    import WaitGen
from cmdcli.generators.guard_gen   import GuardGen
from cmdcli.generators.endturn_gen import EndturnGen
from cmdcli.generators.quit_gen    import QuitGen

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

    def create_command(self, split):
        """
        Creates command from splited text. If command is
        invalid, raise InvalidTextCommand.
        """
        for gen in self.generators:
            if gen.key == split[0]:
                try:
                    return gen.create_command(split[1:])
                except IndexError:
                    raise NotEnoughCmdArgs(split[0])
        raise InvalidCommandKey(split[0])

    def list_commands(self):
        """
        Create a list of descriptions of all commands.
        """
        strlist = [gen.desc for gen in self.generators]
        return strlist
            
class NotEnoughCmdArgs(Exception):
    def __init__(self, string):
        self.message = "No enough arguments for command " + \
            string
        super().__init__(self, self.message)

class InvalidCommandKey(Exception):
    def __init__(self, string):
        self.message = "No command with key " + string
        super().__init__(self, self.message)
