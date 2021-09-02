from duel.attack_state import AttackState

class ReplyState(AttackState):
    """
    State were the opponent reply to an attack.
    """
    def __init__(self, duel, player, opponent, monster, 
        target):
        super().__init__(duel, player, opponent)
        self.name = "REPLY"
        self.monster = monster
        self.target = target
        self.cmddict = {"WAIT"  : self.run_wait_command,
                        "GUARD" : self.run_guard_command}
        
    def run_wait_command(self, cmd):
        """
        Run wait command.
        """
        self.run_undefended_attack(self.monster, self.target)
        self.reply["flags"].append("PLAYERSWITCH")
        from duel.dungeon_state import DungeonState
        nextstate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate

    def run_guard_command(self, cmd):
        """
        Run guard command.
        """
        # perform defended attack
        self.reply["message"] = self.target.name + \
            " defends " + "with " + \
            str(self.target.defense) + "\n"
        damage, damaged = self.monster.\
            attack_defending_monster(self.target)
        self.opponent.crestpool.pay_crests("defense", 1)
        self.add_damage_message(damage, damaged)
        self.check_monster_death(damaged)

        # finish reply and next state
        self.reply["flags"].append("PLAYERSWITCH")
        from duel.dungeon_state import DungeonState
        nextstate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate

    def add_damage_message(self, damage, damaged):
        """
        Add the damage message to the reply given the result
        of an defended attack.
        """
        if damage == 0:
           self.reply["message"] += "No damage inflicted"
        elif damaged is self.target:
            self.reply["message"] += damaged.name + \
                " received " + str(damage) + " damage"
        elif damaged is self.monster:
            self.reply["message"] += damaged.name +  \
                " received " + str(damage) + " damage in " +\
                "retaliation"
