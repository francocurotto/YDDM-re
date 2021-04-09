import urwid
from dice_disp import DiceDisp

class DiceListDisp(urwid.ListBox):
    """
    Displays a list of dice.
    """
    def __init__(self, dice_list):
        # generate list of dice display
        display_list = []
        for dice in dice_list.contents:
            display_list.append(DiceDisp(dice))

        # create walker
        walker = urwid.SimpleFocusListWalker(display_list)
        super().__init__(walker)

    #def keypress(self, size, key):
    #    super().keypress(size, key)
    #    return key
