from duel.duel_state import DuelState

class AttackState(DuelState):
    """
    State were attacks can be performed. Includes dungeon 
    state and reply state.
    """
    def run_undefended_attack(self, monster, target):
        """
        Run undefended attack.
        """
        # deal damage
        damage = monster.attack_monster(target)
        self.reply["damage"] = damage
        # check for monster death
        self.check_monster_death(target)

    def check_monster_death(self, monster):
        """
        Check if monster is death. If True, remove from duel.
        """
        self.reply["kill"] = False
        if monster.is_dead():
            self.duel.remove_summon(monster)
            self.reply["kill"] = True
        
