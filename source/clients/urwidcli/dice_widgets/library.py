import urwid
from urwidcli.dice_widgets.dice import Dice

class Library(urwid.ListBox):
    """
    Displays a list of dice.
    """
    def __init__(self, library):
        # generate widget list
        widgetlist = []
        for dice in library.values():
            index = str(dice.id).zfill(3) + "."
            widgetlist.append(Dice(dice, index))

        # create walker
        walker = urwid.SimpleFocusListWalker(widgetlist)
        super().__init__(walker)
