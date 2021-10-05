import urwid

class Dice(urwid.AttrMap):
    """
    Displays dice information in a single line.
    """
    def __init__(self, dice, index):
        self.dice = dice
        self.index = index
        
        # list of widgets in column
        colwidgets = []

        # create index widget
        colwidgets.append(("pack", urwid.Text(self.index)))

        # create name widget
        name = urwid.Text(self.dice.card.name, wrap="clip")
        colwidgets.append(name)

        # create column and finish widget
        columns = urwid.Columns(colwidgets, dividechars=1)
        super().__init__(columns, None)
