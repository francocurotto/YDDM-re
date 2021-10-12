import urwid
from urwidcli.dice_widgets.dice import Dice

class Pool(urwid.ListBox):
    """
    Displays a dice pool.
    """
    SIZE = 15
    def __init__(self, pool, stringifier):
        self.stringifier = stringifier
        # generate widget list
        widgetlist = []
        for i, dice in enumerate(pool):
            index = str(i+1).rjust(2) + "."
            widgetlist.append(Dice(index, dice, 
                self.stringifier))

        # create walker
        walker = urwid.SimpleFocusListWalker(widgetlist)
        super().__init__(walker)

    def is_full(self):
        """
        True if pool is full.
        """
        return len(self.body) >= self.SIZE

    def add_dice(self, dice):
        """
        Add dice widget to pool.
        """
        # if pool is full, do nothing
        if self.is_full():
            return

        index = str(len(self.body)+1).rjust(2) + "."
        self.body.append(Dice(index, dice, self.stringifier))

    def remove_dice(self, dicewid):
        """
        Remove dice widget from pool.
        """
        self.body.remove(dicewid)
        self.update_index()

    def update_index(self):
        """
        Update the index of all the dice in the pool.
        """
        for i, dicewid in enumerate(self.body):
            index = str(i+1).rjust(2) + "."
            indexwid = dicewid.base_widget.contents[0][0]
            indexwid.set_text(index)
