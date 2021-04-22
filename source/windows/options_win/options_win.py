import urwid
from settings_functions import load_settings
from icon_option import IconOption
from return_button import ReturnButton

class OptionsWin(urwid.Frame):
    """
    Window where the player can change the game settings.
    """
    def __init__(self):
        # get current settings
        self.settings = load_settings()

        # create icons option
        self.icons_opt = IconOption(self.settings)

        # return button
        ret_button = ReturnButton(self.settings)

        # divider
        div = urwid.Divider()

        # pile of all options
        options = urwid.Pile([div, self.icons_opt, div, 
            ret_button])

        super().__init__(urwid.Filler(options, valign="top"))
