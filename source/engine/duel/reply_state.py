from duel.duel_state import DuelState
from dungeon.dicenets.pos import Pos
from player.crest_pool import NotEnoughCrests
from dungeon.dungeon import NotDungeonTile

class DungeonState(DuelState):
    """
    State were monsters move and attack.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "REPLY"
        self.cmddict = {"SKIP"  : self.run_skip_command,
                        "GUARD" : self.run_guard_command}
        
    def run_skip_command(self, cmd):
        """
        Run skip command.
        """
        pass

    def run_guard_command(self, cmd):
        """
        Run guard command.
        """
        pass
