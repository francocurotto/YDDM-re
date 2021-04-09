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
        self.library_disp = DiceListDisp(library)

        # create summon display
        dice = self.library_disp.focus.dice
        self.summon_disp = SummonDisp(dice.card)

        # create right column
        right_col = urwid.Pile([
            (10, urwid.LineBox(self.summon_disp,
                "Summon Information", "left"))])

        # create body
        body_cols = urwid.Columns([
            urwid.LineBox(self.library_disp,
                "Dice Library", "left"),
            right_col])
        body = urwid.Padding(body_cols, align="center",
            width=67*2)
    
        # create footer
        footer = urwid.Text("↑,↓:Select dice")
        super().__init__(body, footer=footer)

    def keypress(self, size, key):
        # if up/down arrows, change summon display
        if key in ["up", "down"]:
            self.contents["body"][0].keypress(size, key)
            dice = self.get_focus_widgets()[-2].dice
            self.summon_disp.update(dice.card)
