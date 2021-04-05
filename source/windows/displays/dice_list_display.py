import urwid
from dice_display import DiceDisplay

class DiceListDisplay(urwid.ListBox):
    """
    Displays a list of dice.
    """
    def __init__(self, dice_list):
        # generate list of dice display
        display_list = []
        for dice in dice_list.contents:
            display_list.append(DiceDisplay(dice))

        # create walker
        walker = urwid.SimpleFocusListWalker(display_list)
        super().__init__(walker)
