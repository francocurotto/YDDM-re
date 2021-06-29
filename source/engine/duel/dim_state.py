from duel.duel_state import DuelState
from dungeon.dicenets.net_dict import net_dict

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
        dice = self.dimdice[cmd["dice"]]

        # get the summon from the dice
        summon = dice.card.summon()

        # add dice to dimensioned dice
        self.player.dimdice.append(dice)

        # create net
        net = net_dict[cmd["net"]]()

        # apply transformations to net
        net.apply_trans(cmd["trans"])

        # dimension the dice
        self.duel.dungeon.set_net(net, cmd["pos"], 
            self.player, summon)

        # fill success reply
        self.reply["message"] = "Dimension The Dice!"
        #TODO: define dungeon state
        return self.reply, self

    def run_skip_command(self, cmd):
        """
        Run skip command.
        """
        # fill success reply
        self.reply["valid"] = True
        self.reply["message"] = "Dimension skiped"
        #TODO: define dungeon state
        return self.reply, self
