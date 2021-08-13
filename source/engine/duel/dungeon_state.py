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
        dest = Pos(*cmd["dest"])

        # error prone tasks
        try:
            monster = self.get_player_monster(origin)
            target = self.get_opponent_target(dest)
            self.check_attack_range(origin, dest)
            self.pay_attack_cost()
        except self.attackerrors as e:
            self.reply["message"] = e.message
            return self.reply, self

        # check for monster or ml attack
        if target.is_monster():
            nextstate = self.run_monster_attack(monster,   
                target)
        elif target.is_monster_lord():
            nextstate = self.run_ml_attack(monster)
    
        return self.reply, nextstate

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

    def run_monster_attack(self, monster, target):
        """
        Run the attack from a player monster to an opponent
        monster.
        """
        power = monster.get_attack_power(target)
        self.reply["message"] = monster.name + " attacks " +\
            target.name + " with " + power

        # if opponent can defend, go to next state
        #if self.opponent.crestpool.defense > 0:
        #    from reply_state import ReplyState
        #    return ReplyState(self.duel, self.player, 
        #        self.opponent, monster, target)

        # if opponent cannot defend, continue with attack
        damage = monster.attack_monster(target)
        self.reply["message"] += "\n" + self.opponent.name +\
            " cannot defend\n" + target.name + \
            " received " + str(damage) + " damage"
        return self

    def run_ml_attack(self, monster):
        """
        Run the attack from a player monster to the opponent
        monster lord.
        """
        self.reply["message"] = monster.name + " attacks " +\
            self.opponent.name + " monster lord"
        self.monster.attack_ml(self.opponent)

        # check for opponent loss
        if self.opponent.ml.hearts <= 0:
            self.reply["message"] = ".\n" + \
                self.opponent.name + " lost all their " + \
                " hearts.\n" + self.player.name " is the " + \
                "winner!"
            from end_state import EndState
            return EndState(self.duel, self.player,
                self.opponent)
        return self

    def get_player_monster(self, pos):
        """
        Get player moster at position pos. If no player
        monster in pos, return exception.
        """
        monster = self.duel.dungeon.get_content(pos)
        if monster not in self.player.monsters:
            raise NotPlayerMonster(pos)
        return monster

    def get_opponent_target(self, pos):
        """
        Get opponent targer at position pos. If no opponent
        target in pos, return exception.
        """
        target = self.duel.dungeon.get_content(pos)
        if target not in self.opponent.monsters or \
            target not self.opponent.ml:
            raise NotOpponentTarget(pos)
        return target

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

    def check_attack_range(origin, dest):
        """
        Check if an attack is in attack range.
        """
        return origin.distance_to(dest) == 1

    def pay_attack_cost(self):
        """
        Pay the attack cost of an attack.
        """
        self.player.crestpool.remove_crests("attack", 1)

class NotPlayerMonster(Exception):
    def __init__(self, pos):
        self.message = "No player monster at " + str(pos)
        super().__init__(self.message)

class NotOpponentTarget(Exception):
    def __init__(self, pos):
        self.message = "No opponent targer at " + str(pos)
        super().__init__(self.message)

class NotPathFound(Exception):
    def __init__(self, origin, dest):
        self.message = "No path found between " + \
            str(origin) + " and " + str(dest)
        super().__init__(self.message)
