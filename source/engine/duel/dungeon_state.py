from duel.duel_state import DuelState
from dungeon.dicenets.pos import Pos

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
        if cmd["command"] == "MOVE":
            return self.run_move_command(cmd)
        elif cmd["command"] == "ENDTURN":
            return self.run_endturn_command(cmd)
        return super().update(cmd)

    def run_move_command(self, cmd):
        """
        Run move command.
        """
        # 1. chack monster at origin
        origin = Pos(*cmd["origin"])
        dungobj = self.duel.dungeon.get_content(origin)
        if not dungobj in self.player.monsters:
            self.reply["Message"] = "No player monster at "+\
                "origin"
            return self.reply, self

        # 2. check destiny is unoccupied
        dest = Pos(*cmd["dest"])
        dungobj = self.duel.dungeon.get_content(dest)
        if dungobj.is_target():
            self.reply["Message"] = "Destination ocupied"
            return self.reply, self

        # 3. check if monster has already move

        # 4. check valid path

        # 5. check enough movement crests


    def run_endturn_command(self, cmd):
        """
        Run endturn command.
        """
        # fill success reply
        self.reply["valid"] = True
        self.reply["newturn"] = True
        self.reply["message"] = "Turn finished!"
        from duel.roll_state import RollState
        nextstate = RollState(self.duel, self.opponent, 
            self.player)
        return self.reply, nextstate
