import urwid
from icon_option import IconOption
from return_button import ReturnButton

class OptionsWin(urwid.Frame):
    """
    Window where the player can change the game settings.
    """
    def __init__(self):
        # create icons option
        self.icons_opt = IconOption()

        # return button
        ret_button = ReturnButton()

        # divider
        div = urwid.Divider()

        # pile of all options
        options = urwid.Pile([div, self.icons_opt, div, 
            ret_button])

        super().__init__(urwid.Filler(options, valign="top"))
