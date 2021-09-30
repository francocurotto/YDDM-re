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
        # check for monster death
        self.check_monster_death(target)

    def check_monster_death(self, monster):
        """
        Check if monster is death. If True, remove from duel
        and add message to reply.
        """
        reply["kill"] = False
        if monster.is_dead():
            self.duel.remove_summon(monster)
            reply["kill"] = True
        
