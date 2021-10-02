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
        self.reply["result"] = "WAIT"
        self.reply["target"] = self.target.name
        self.reply["flags"].append("PLAYERSWITCH")
        self.run_undefended_attack(self.monster, self.target)
        from duel.dungeon_state import DungeonState
        nextstate = DungeonState(self.duel, self.player, 
            self.opponent)
        self.reply["valid"] = True
        self.reply["result"] = "WAIT"
        return self.reply, nextstate

    def run_guard_command(self, cmd):
        """
        Run guard command.
        """
        # perform defended attack
        damage, damaged = self.monster.\
            attack_defending_monster(self.target)
        self.opponent.crestpool.pay_crests("defense", 1)
        self.check_monster_death(damaged)
        retal = True if damaged is self.monster else False

        # finish reply and next state
        self.reply["valid"] = True
        self.reply["result"] = "GUARD"
        self.reply["monster"] = self.monster.name
        self.reply["target"] = self.target.name
        self.reply["defense"] = self.target.defense
        self.reply["retaliation"] = retal
        self.reply["damage"] = damage
        self.reply["flags"].append("PLAYERSWITCH")
        from duel.dungeon_state import DungeonState
        nextstate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate
