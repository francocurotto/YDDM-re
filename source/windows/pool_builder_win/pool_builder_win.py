import urwid
from globvars import library_path
from dice_list import DiceList
from dice_list_display import DiceListDisplay

class PoolBuilderWin(urwid.Frame):
    """
    Window where the player can build dice pools.
    """
    def __init__(self):
        # create library display
        library = DiceList(library_path)
        lib_display = urwid.LineBox(DiceListDisplay(library),
            "Dice Library", "left")

        # create body
        body_cols = urwid.Columns([lib_display])
        body = urwid.Padding(body_cols, align="center",
            width=63)
    
        # create footer
        footer = urwid.Text("↑,↓:Select dice")
        super().__init__(body, footer=footer)

