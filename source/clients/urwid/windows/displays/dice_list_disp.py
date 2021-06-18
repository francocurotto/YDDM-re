import urwid
from dice_disp import DiceDisp

class DiceListDisp(urwid.ListBox):
    """
    Displays a list of dice.
    """
    def __init__(self, dice_list, disp_id=False):
        # generate list of dice display
        display_list = []
        for dice in dice_list:
            display_list.append(DiceDisp(dice, disp_id))

        # create walker
        walker = urwid.SimpleFocusListWalker(display_list)
        super().__init__(walker)
