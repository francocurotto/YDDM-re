from duel.duel_state import DuelState
from dungeon.dicenets.netdict import netdict
from dungeon.dicenets.pos import Pos

class DimState(DuelState):
    """
    State were the player dimension the dice.
    """
    def __init__(self, duel, player, opponent, dimdice):
        super().__init__(duel, player, opponent)
        self.name = "DIM"
        self.dimdice = dimdice

    def update(self, cmd):
        """
        Update state given command cmd.
        """
        if cmd["command"] == "DIM":
            return self.run_dim_command(cmd)
        elif cmd["command"] == "SKIP":
            return self.run_skip_command(cmd)
        return super().update(cmd)

    def run_dim_command(self, cmd):
        """
        Run dim command.
        """
        # get the selected dice
        try:
            dice = self.dimdice[cmd["dice"]]
        except IndexError:
            self.reply["message"] = "Invalid dice index " + \
                str(cmd["dice"])
            return self.reply, self

        # get the summon from the dice
        summon = dice.card.summon()

        # add dice to dimensioned dice
        self.player.dimdice.append(dice)

        # create net
        net = netdict[cmd["net"]]()

        # apply transformations to net
        net.apply_trans(cmd["trans"])

        # apply offset
        net.offset(Pos(*cmd["pos"]))

        # dimension the dice
        success, message = self.duel.dungeon.set_net(net, 
            self.player, summon)
        if not success:
            self.reply["message"] = message
            return self.reply, self

        # fill success reply
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
