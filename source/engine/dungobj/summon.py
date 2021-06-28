from dungobj.dungobj import DungeonObject

class Summon(DungeonObject):
    """
    Summon created from a dice dimension.
    """
    def __init__(self, card):
        # attributes extracted from card
        self.name = card.name
        self.level = card.level
        self.ability = card.ability
        self.card = card
