from dungobj.summon import Summon

class Monster(Summon):
    """
    A monster in the board.
    """
    def __init__(self, card):
        super().__init__(card)

        # attributes extracted from card
        self.attack = self.card.attack
        self.defense = self.card.defense
        self.life = self.card.life
        self.cooldown = False

    def add_to_player(self, player):
        """
        Add monster to the proper player list when summoning.
        """
        super().add_to_player(player)
        player.monsters.append(self)

    def remove_from_player(self, player):
        """
        Remove summon from proper player list.
        """
        super().remove_from_player(player)
        player.monsters.remove(self)

    def is_dead(self):
        """
        True if monster is dead.
        """
        return self.life <= 0

    def attack_monster(self, target):
        """
        Attack the target monster.
        """
        power = self.get_attack_power(target)
        target.life -= power
        self.cooldown = True
        return power

    def attack_ml(self, opponent):
        """
        Attack the opponent monster lord, directly removing
        one of its hearts.
        """
        opponent.ml.hearts -= 1
        self.attack_cooldown = True

    def attack_defending_monster(self, target):
        """
        Attack a monster that is defending. Return damage 
        given and monster damaged with the attack.
        """
        # get attack power
        power = self.get_attack_power(target)

        # if attack surpass defense, inflict damage in 
        # target monster
        if power >= target.defense:
            damage = power - target.defense
            target.life -= damage
            return damage, target

        # if defense surpass attack, inflict 
        # retaliation damage in attacker monster
        elif power < target.defense:
            damage = target.defense - power
            target.life -= damage
            return damage, self

    def get_attack_power(self, target):
        """
        Get attacking power when attacking a monster,
        considering type advantages.
        """
        # case advantage
        if self.has_advantage(target):
            return self.attack + 10
        # case disadvantage
        elif self.has_disadvantage(target):
            return max(self.attack - 10, 0)
        # case neutral
        else:
            return self.attack

    def has_advantage(self, target):
        """
        Check if monster has type advantage over target 
        monster. This can be implemented easily by checking
        the reverse condition, ie, if the target has 
        disadvantage (that is already implemented).
        """
        return target.has_disadvantage(self)

    def is_monster(self):
        return True

    # default advantage functions
    def has_advantage_over_spellcaster(self):
        return False
    def has_advantage_over_warrior(self):
        return False
    def has_advantage_over_undead(self):
        return False
    def has_advantage_over_beast(self):
        return False
    def has_advantage_over_dragon(self):
        return False
