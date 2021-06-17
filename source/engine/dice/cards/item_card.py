from summon_card import SummonCard

class ItemCard(SummonCard):
    """
    Object that contains the information of an item.
    """
    def __init__(self, info):
        super().__init__(info)

    def is_item(self):
        return True
