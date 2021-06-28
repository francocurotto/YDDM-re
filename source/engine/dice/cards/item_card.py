from dice.cards.summon_card import SummonCard
from dungobj.item import Item

class ItemCard(SummonCard):
    """
    Object that contains the information of an item.
    """
    def __init__(self, info):
        super().__init__(info)

    def is_item(self):
        return True

    def summon(self):
        """
        Return a summon based on card.
        """
        return Item(self)
