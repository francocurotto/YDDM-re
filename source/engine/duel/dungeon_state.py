from duel.attack_state import AttackState
from dungeon.dicenets.pos import Pos
from errors import NotPlayerMonster
from errors import NotOpponentTarget
from errors import AttackOutOfRange
from errors import MonsterInCooldown
from errors import NotPathFound
from errors import NotEnoughCrests
from errors import NotDungeonTile

class DungeonState(AttackState):
    """
    State were monsters move and attack.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "DUNGEON"
        self.cmddict = {"MOVE"    : self.run_move_command,
                        "ATTACK"  : self.run_attack_command,
                        "ENDTURN" : self.run_endturn_command}
        self.errors = (NotDungeonTile, NotPlayerMonster,
            NotOpponentTarget, NotPathFound, 
            AttackOutOfRange, MonsterInCooldown,
            NotEnoughCrests)
        
    def run_move_command(self, cmd):
        """
        Run move command.
        """
        origin = Pos(*cmd["origin"])
        dest = Pos(*cmd["dest"])
        
        # move monster
        monster = self.get_player_monster(origin)
        path = self.get_path(origin, dest)
        self.pay_movement_cost(path)
        self.duel.dungeon.move_dungobj(origin, dest)

        # fill success reply
        self.reply["valid"] = True
        self.reply["message"] = monster.name + " moved " + \
            "from " + str(origin) + " to " + str(dest)
        return self.reply, self

    def run_attack_command(self, cmd):
        """
        Run attack command.
        """
        # get origin, dest position and tile
        origin = Pos(*cmd["origin"])
        dest = Pos(*cmd["dest"])

        # get attack info
        monster = self.get_player_monster(origin)
        target = self.get_opponent_target(dest)
        self.check_attack_range(origin, dest)
        self.check_cooldown(monster)
        self.player.crestpool.pay_crests("attack", 1)

        # check for monster or ml attack
        monster.cooldown = True
        if target.is_monster():
            nextstate = self.run_monster_attack(monster,   
                target)
        elif target.is_monster_lord():
            nextstate = self.run_ml_attack(monster)
    
        # fill success reply
        self.reply["valid"] = True
        return self.reply, nextstate

    def run_endturn_command(self, cmd):
        """
        Run endturn command.
        """
        # reset cooldown from player monsters
        self.player.reset_cooldown()

        # fill success reply
        self.reply["valid"] = True
        self.reply["message"] = "Turn finished!"
        self.reply["flags"].append("PLAYERSWITCH")
        self.reply["flags"].append("NEWTURN")
        from duel.roll_state import RollState
        nextstate = RollState(self.duel, self.opponent, 
            self.player)
        return self.reply, nextstate

    def run_monster_attack(self, monster, target):
        """
        Run the attack from a player monster to an opponent
        monster.
        """
        # get the attaking power message
        self.add_attack_message(monster, target)

        # if opponent can defend, go to next state
        if self.opponent.crestpool.defense > 0:
            self.reply["flags"].append("PLAYERSWITCH")
            from duel.reply_state import ReplyState
            return ReplyState(self.duel, self.player, 
                self.opponent, monster, target)

        # if opponent cannot defend, continue with attack
        self.reply["message"] += "\n" + self.opponent.name +\
            " cannot defend\n"
        self.run_undefended_attack(monster, target)
        return self

    def run_ml_attack(self, monster):
        """
        Run the attack from a player monster to the opponent
        monster lord.
        """
        self.reply["message"] = monster.name + " attacks " +\
            self.opponent.name + " monster lord"
        monster.attack_ml(self.opponent)

        # check for opponent loss
        if self.opponent.ml.hearts <= 0:
            self.reply["flags"].append("ENDDUEL")
            self.reply["message"] += ".\n" + \
                self.opponent.name + " lost all their " + \
                "hearts.\n" + self.player.name + \
                " is the winner!"
            from duel.endduel_state import EndDuelState
            return EndDuelState(self.duel, self.player,
                self.opponent)
        return self

    def get_player_monster(self, pos):
        """
        Get player moster at position pos. If no player
        monster in pos, return exception.
        """
        monster = self.duel.dungeon.get_content(pos)
        if monster not in self.player.monsters:
            raise NotPlayerMonster(pos.totuple())
        return monster

    def get_opponent_target(self, pos):
        """
        Get opponent targer at position pos. If no opponent
        target in pos, return exception.
        """
        target = self.duel.dungeon.get_content(pos)
        if target not in self.opponent.monsters and \
            target is not self.opponent.ml:
            raise NotOpponentTarget(pos.totuple())
        return target

    def get_path(self, origin, dest):
        """
        Get a path from origin to dest from the dungeon. If
        not path was found, raise exception.
        """
        path = self.duel.dungeon.get_path(origin, dest)
        if path is None:
            raise NotPathFound(origin.totuple(), 
                dest.totuple())
        return path

    def pay_movement_cost(self, path):
        """
        Pay the movement cost of a monster given a path.
        """
        cost = len(path)-1
        self.player.crestpool.pay_crests("movement", cost)

    def check_attack_range(self, origin, dest):
        """
        Raise an error if attack is out or range.
        """
        if origin.distance_to(dest) != 1:
            raise AttackOutOfRange

    def check_cooldown(self, monster):
        """
        Raise an error if monster is in cooldown.
        """
        if monster.cooldown:
            raise MonsterInCooldown(monster.name)

    def add_attack_message(self, monster, target):
        """
        Add attack power message to reply.
        """
        # create advantage message
        if monster.has_advantage(target):
            self.reply["message"] += monster.name + \
                " has advantage over " + target.name + "\n"
        elif monster.has_disadvantage(target):
            self.reply["message"] += monster.name + \
                " has disadvantage over " + target.name+"\n"
        # create power message
        power = monster.get_attack_power(target)
        self.reply["message"] += monster.name + \
            " attacks " + target.name + " with " + str(power)
