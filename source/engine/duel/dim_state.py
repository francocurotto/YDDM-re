from duel.duel_state import DuelState
from dungeon.dicenets.netdict import netdict
from dungeon.dicenets.pos import Pos
from dungeon.dungeon import NetUnconnectedError
from dungeon.dungeon import TilePosUnboundError
from dungeon.dungeon import TileOverlapsError

class DimState(DuelState):
    """
    State were the player dimension the dice.
    """
    def __init__(self, duel, player, opponent, dimdice):
        super().__init__(duel, player, opponent)
        self.name = "DIM"
        self.dimdice = dimdice
        self.cmddict = {"DIM"  : self.run_dim_command,
                        "SKIP" : self.run_skip_command}
        self.dimerrors = (DimIndexError, NetUnconnectedError,
            TilePosUnboundError, TileOverlapsError)

    def run_dim_command(self, cmd):
        """
        Run dim command.
        """
        net = netdict[cmd["net"]]()
        net.apply_trans(cmd["trans"])
        net.offset(Pos(*cmd["pos"]))

        # get the selected dice
        try:
            dice = self.get_dimdice(cmd["dice"])
            summon = dice.card.summon()
            self.duel.dungeon.set_net(net,self.player,summon)
        except self.dimerrors as e:
            self.reply["message"] = e.message
            return self.reply, self

        # add dice to dimensioned dice
        self.player.dimdice.append(dice)

        # fill success reply
        self.reply["valid"] = True
        self.reply["message"] = "Dimension The Dice!"
        from duel.dungeon_state import DungeonState
        nextstate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate

    def run_skip_command(self, cmd):
        """
        Run skip command.
        """
        # fill success reply
        self.reply["valid"] = True
        self.reply["message"] = "Dimension skipped"
        from duel.dungeon_state import DungeonState
        nextstate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate

    def get_dimdice(self, i):
        """
        Get dimension dice from index. Raise error if invalid
        index.
        """
        try:
            return self.dimdice[i]
        except IndexError:
            raise DimIndexError

class DimIndexError(Exception):
    message = "Invalid dimension index"
