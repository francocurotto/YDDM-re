from duel.duel_state import DuelState

class DungeonState(DuelState):
    """
    State were the opponent reply to an attack.
    """
    def __init__(self, duel, player, opponent, monster, 
        target):
        super().__init__(duel, player, opponent)
        self.name = "REPLY"
        self.monster = monster
        self.target = target
        self.cmddict = {"SKIP"  : self.run_skip_command,
                        "GUARD" : self.run_guard_command}
        
    def run_skip_command(self, cmd):
        """
        Run skip command.
        """
        self.run_undefended_attack(self.monster, self.target)
        self.reply["flags"].append("PLAYERSWITCH")
        nextsate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate

    def run_guard_command(self, cmd):
        """
        Run guard command.
        """
        # perform defended attack
        self.reply["message"] = self.target + " defends " + \
            "with " + str(self.target.defense) + "\n"
        damage, damaged = self.monster.\
            attack_defending_monster(self.target)
        #self.reply["message"] += affected.name + \
        #    " received " + str(damage) + " damage"
        self.add_damage_message(self, damage, damaged)#TODO
        self.check_monster_death(affected)

        # finish reply and next state
        self.reply["flags"].append("PLAYERSWITCH")
        nextsate = DungeonState(self.duel, self.player, 
            self.opponent)
        return self.reply, nextstate
