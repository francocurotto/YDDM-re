from dungobj.summon import Summon

class Item(Summon):
    """
    An item in the board.
    """
    def __init__(self, card):
        super().__init__(card)

    def add_to_player(self, player):
        """
        Add item to the proper player list when summoning.
        """
        player.items.append(self)

    def is_item(self):
        return True
