from duel.duel_state import DuelState
from dungeon.dicenets.pos import Pos
from player.crest_pool import NotEnoughCrests

class DungeonState(DuelState):
    """
    State were monsters move and attack.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "DUNGEON"
        self.cmddict = {"MOVE"    : self.run_move_command,
                        "ATTACK"  : self.run_attack_command,
                        "ENDTURN" : self.run_endturn_command}
        self.moveerrors = (NotDungeonTile,
            NotPlayerMonster, NotPathFound, NotEnoughCrests)
        
    def run_move_command(self, cmd):
        """
        Run move command.
        """
        origin = Pos(*cmd["origin"])
        dest = Pos(*cmd["dest"])
        
        # error prone tasks
        try:
            monster = self.get_player_monster(origin)
            path = self.get_path(origin, dest)
            self.pay_movement_cost(path)
            self.duel.dungeon.move_dungobj(origin, dest)
        except self.moveerrors as e:
            self.reply["message"] = e.message
            return self.reply, self

        self.reply["valid"] = True
        self.reply["message"] = monster.name + " moved " + \
            "from " + str(origin) + " to " + str(dest)
        nextstate = DungeonState(self.duel, self.opponent, 
            self.player)
        return self.reply, nextstate

    def run_attack_command(self, cmd):
        """
        Run attack command.
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

        # 3. check target at destination
        target = desttile.content
        if not self.opponent.is_my_target(target):
            self.reply["message"] = "No opponent target " + \
                "at destination"
            return self.reply, self

        # 4. check monster range
        if monster.range < origin.distance_to(dest):
            self.reply["message"] = "Target out of range"
            return self.reply, self

        # 5. check enough attack crests
        if self.player.crestpool.attack < 1:
            self.reply["message"] = "Not enough attack " + \
                "crests"
            return self.reply, self
            
        # 6. attack is valid, first reduce attack crest
        self.duel.player.crestpool.attack -= 1

        # 7. if target is monster
        if target.is_monster():
            self.reply["message"] = monster.name + " is " + \
                "attacks " + target.name + " with " + \
                str(monster.get_attacking_power()) + " power"
            if self.opponent.can_reply(target):
                from duel.reply_state import ReplyState
                nextstate = ReplyState(self, self.duel, 
                    self.player, self.oppoent, monster, 
                    target)
                return self.reply, nextstate
            else:
                monster.attack_monster(target, 
                    defending=False)

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

    def get_player_monster(self, pos):
        """
        Get player moster at position pos. If no player
        monster in pos, return exception.
        """
        monster = self.duel.dungeon.get_content(pos)
        if monster not in self.player.monsters:
            raise NotPlayerMonster(pos)
        return monster

    def get_path(self, origin, dest):
        """
        Get a path from origin to dest from the dungeon. If
        not path was found, raise exception.
        """
        path = self.duel.dungeon.get_path(origin, dest)
        if path is None:
            raise NotPathFound(origin, dest)
        return path

    def pay_movement_cost(self, path):
        """
        Pay the movement cost of a monster given a path.
        """
        cost = len(path)-1
        self.player.crestpool.remove_crests("movement", cost)

class NotPlayerMonster(Exception):
    def __init__(self, pos):
        self.message = "No player monster at " + str(pos)
        super().__init__(self.message)

class NotPathFound(Exception):
    def __init__(self, origin, dest):
        self.message = "No path found between " + \
            str(origin) + " and " + str(dest)
        super().__init__(self.message)
