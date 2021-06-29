from dungobj.monster import Monster

class Dragon(Monster):
    """
    A monster of type dragon.
    """
    def __init__(self, card):
        super().__init__(card)

    def has_advantage_over_spellcaster(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_dragon()
