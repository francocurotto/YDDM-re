import urwid

class DiceInfo(urwid.Text):
    """
    Displays dice information in text format.
    """
    def __init__(self, dice, stringifier):
        self.stringifier = stringifier
        string = self.stringifier.stringify_dice(dice)
        super().__init__(string)

    def update(self, dice):
        """
        Update text with new dice information.
        """
        self.set_text(self.stringifier.stringify_dice(dice))
        

