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
        opponent.monster_lord.hearts -= 1
        self.attack_cooldown = True

    #def attack_defending_monster(self, attacked, power):
    #    """
    #    Attack a monster that is defending with power attack
    #    points.
    #    """
    #    # defending message
    #    self.log.add(attacked.name + " defends with " + \
    #        str(attacked.defense) + ".\n")

    #    # if attack surpass defense, inflict damage in 
    #    # attacked monster
    #    if power > attacked.defense:
    #        damage = power - attacked.defense
    #        attacked.life -= damage
    #        self.log.add(attacked.name + " received " + \
    #            str(damage) + " points of damage.\n")

    #    # if defense surpass attack, get retaliation damage
    #    # in attacker monster
    #    elif power < attacked.defense:
    #        damage = attacked.defense - power
    #        self.inflict_retaliation_damage(damage)
    #    
    #    # attack and defense are equal
    #    else:
    #        self.log.add("No damage inflicted.\n")

    def get_attack_power(self, target):
        """
        Get attacking power when attacking a monster,
        considering type advantages.
        """
        # case advantage
        if self.has_advantage(attacked):
            return self.attack + 10
        # case disadvantage
        elif self.has_disadvantage(attacked):
            return self.attack - 10
        # case neutral
        else:
            return self.attack

    #def inflict_retaliation_damage(self, damage):
    #    """
    #    Inflict the damage for attacking a defending monster
    #    that has higher defense that the attack of the 
    #    attacker. Note: should consider different rules.
    #    """
    #    # case retaliation damage is activated
    #    if retal_dmg:
    #        self.life -= damage
    #        self.log.add(self.name + " received " + \
    #            str(damage) + " points of damage in " + \
    #            "retaliation.\n")
    #    # case retaliation damage deactivated
    #    else:
    #       self.log.add("No damage inflicted.\n")
            
    def has_advantage(self, attacked):
        """
        Check if monster has type advantage over attacked 
        monster. This can be implemented easily by checking
        the reverse condition, ie, if the attacked has 
        disadvantage (tht is already implemented).
        """
        return attacked.has_disadvantage(self)

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
