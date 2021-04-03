import urwid

class DiceDisplay(urwid.Columns):
    """
    Displays dice information in a single line.
    """
    def __init__(self, dice_info):
        dice_name = urwid.Filler(
            urwid.Text(dice_info["NAME"]))
        super().__init__([dice_name])
