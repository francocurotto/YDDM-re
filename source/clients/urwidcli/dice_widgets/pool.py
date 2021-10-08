import urwid
from urwidcli.dice_widgets.dice import Dice

class Pool(urwid.ListBox):
    """
    Displays a dice pool.
    """
    def __init__(self, pool, stringifier):
        # generate widget list
        widgetlist = []
        for i, dice in enumerate(pool):
            index = str(i+1).rjust(2) + "."
            widgetlist.append(Dice(index, dice, stringifier))

        # create walker
        walker = urwid.SimpleFocusListWalker(widgetlist)
        super().__init__(walker)
