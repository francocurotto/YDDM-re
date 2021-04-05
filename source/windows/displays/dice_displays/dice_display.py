import urwid
from icon_functions import load_icons

class DiceDisplay(urwid.AttrMap):
    """
    Displays dice information in a single line.
    """
    def __init__(self, dice):
        icons = load_icons()

        # define each column widget
        name = urwid.Filler(urwid.Text(dice.card.name))
        #name = urwid.Text(dice.card.name)
        type = urwid.Filler(urwid.Text(icons["TYPE_"+dice.card.type]))
        #type = urwid.Text(icons["TYPE_"+dice.card.type])
        #col_widgets = [name, ("pack", type)]
        #col_widgets = [name, (1, type)]
        col_widgets = [name, type]

        columns = urwid.Columns(col_widgets, dividechars=1)

        super().__init__(columns, None)
