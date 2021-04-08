import urwid
from globvars import library_path
from dice_list import DiceList
from dice_list_disp import DiceListDisp
from summon_disp import SummonDisp

class PoolBuilderWin(urwid.Frame):
    """
    Window where the player can build dice pools.
    """
    def __init__(self):
        # create library display
        library = DiceList(library_path)
        library_disp = urwid.LineBox(DiceListDisp(library), 
            "Dice Library", "left")

        # create summon display
        dice = library_disp.original_widget.focus.dice
        summon_disp = urwid.LineBox(SummonDisp(dice.card), 
            "Summon Information", "left")

        # create right column
        right_col = urwid.Pile([(10,summon_disp)])

        # create body
        body_cols = urwid.Columns([library_disp, 
            right_col])
        body = urwid.Padding(body_cols, align="center",
            width=63*2)
    
        # create footer
        footer = urwid.Text("↑,↓:Select dice")
        super().__init__(body, footer=footer)

