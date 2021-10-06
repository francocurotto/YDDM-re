import urwid
from urwidcli.dice_widgets.dice import Dice

class Library(urwid.ListBox):
    """
    Displays a list of dice.
    """
    def __init__(self, library, stringifier):
        # generate widget list
        widgetlist = []
        for dice in library.values():
            index = str(dice.id).zfill(3) + "."
            widgetlist.append(Dice(stringifier, index, dice))

        # create walker
        walker = urwid.SimpleFocusListWalker(widgetlist)
        super().__init__(walker)
