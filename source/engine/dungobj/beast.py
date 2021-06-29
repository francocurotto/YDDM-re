from dungobj.monster import Monster

class Beast(Monster):
    """
    A monster of type beast.
    """
    def __init__(self, card):
        super().__init__(card)

    def has_advantage_over_warrior(self):
        return True

    def has_disadvantage(self, monster):
        return monster.has_advantage_over_beast()
