from duel.duel_state import DuelState

class DungeonState(DuelState):
    """
    State were monsters move and attack.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "DUNGEON"
        
    def update(self, cmd):
        """
        Update state given command cmd.
        """
        if cmd["command"] == "ENDTURN":
            return self.run_endturn_command(cmd)
        return super().update(cmd)

    def run_endturn_command(self, cmd):
        """
        Run endturn command.
        """
        # fill success reply
        self.reply["valid"] = True
        self.reply["newturn"] = True
        self.reply["message"] = "Turn finished"
        from duel.roll_state import RollState
        nextstate = RollState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate
