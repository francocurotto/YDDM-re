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
        # get origin, dest position and tile
        origin = Pos(*cmd["origin"])
        origintile = self.duel.dungeon.get_tile(origin)
        dest = Pos(*cmd["dest"])
        desttile = self.duel.dungeon.get_tile(dest)

        # 1. check if origin and dest are dungeon tiles
        if not origintile.is_dungeon():
            self.reply["message"] = "Origin not dungeon tile"
            return self.reply, self
        if not desttile.is_dungeon():
            self.reply["message"] = "Destination not "+ \
                "dungeon tile"
            return self.reply, self

        # 2. check monster at origin
        monster = origintile.content
        if not monster in self.player.monsters:
            self.reply["message"] = "No player monster at "+\
                "origin"
            return self.reply, self

        # 3. check destiny is unoccupied
        if desttile.content.is_target():
            self.reply["message"] = "Destination occupied"
            return self.reply, self

        # 4. check valid path
        path = self.duel.dungeon.get_path(origin, dest)
        if not path:
            self.reply["message"] = "Cannot reach destination"
            return self.reply, self

        # 5. check enough movement crests
        movecost = len(path) - 1 # first pos doesn't count
        if self.player.crestpool.movement < movecost:
            self.reply["message"] = "Not enough movement " +\
                "crests"
            return self.reply, self

        # 6. everything is okay, so move the monster
        self.player.crestpool.movement -= movecost
        self.duel.dungeon.move_dungobj(origin, dest)
        self.reply["message"] = monster.name + " moved " + \
            "from " + str(origin) + " to " + str(dest)
        return self.reply, self 

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
