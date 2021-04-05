import urwid
from globvars import library_path
from dice_list import DiceList
from dice_list_display import DiceListDisplay

class PoolBuilderWin(urwid.Frame):
    """
    Window where the player can build dice pools.
    """
    def __init__(self):
        # create library
        library = DiceList(library_path)
        lib_display = DiceListDisplay(library)
        footer = urwid.Text("Instructions for window go here")
        super().__init__(lib_display, footer=footer)

