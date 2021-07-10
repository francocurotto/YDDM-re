from dungobj.dungobj import DungeonObject

class Summon(DungeonObject):
    """
    Summon created from a dice dimension.
    """
    def __init__(self, card):
        # attributes extracted from card
        self.name = card.name
        self.type = card.type
        self.level = card.level
        self.ability = card.ability
        self.card = card

    def add_to_player(self, player):
        """
        Add summon to the proper player list when summoning.
        """
        player.summons.append(self)

    def is_summon(self):
        return True
