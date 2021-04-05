import urwid
from globvars import library_path
from dice_list import DiceList
#from library_display import LibraryDisplay
from dice_display import DiceDisplay

class PoolBuilderWin(urwid.Frame):
    """
    Window where the player can build dice pools.
    """
    def __init__(self):
        # create library
        library = DiceList(library_path)
        #lib_display = DiceListDisplay(library)
        footer = urwid.Text("Instructions for window go here")
        super().__init__(DiceDisplay(library.contents[0]), footer=footer)

