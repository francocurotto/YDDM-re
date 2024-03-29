import urwid
from urwidcli.dice_widgets.dice import Dice

class Library(urwid.ListBox):
    """
    Displays a library.
    """
    def __init__(self, library, stringifier):
        # generate widget list
        widgetlist = []
        for dice in library.values():
            index = str(dice.id).rjust(3) + "."
            widgetlist.append(Dice(index, dice, stringifier))

        # create walker
        walker = urwid.SimpleFocusListWalker(widgetlist)
        super().__init__(walker)
