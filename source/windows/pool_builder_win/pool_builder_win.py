import urwid
from globvars import library
from dicesets_functions import create_dice_list
from dice_lib_disp import DiceLibDisp
from dice_list_disp import DiceListDisp
from summon_disp import SummonDisp

class PoolBuilderWin(urwid.Frame):
    """
    Window where the player can build dice pools.
    """
    def __init__(self):
        # create library display
        self.library_disp = DiceLibDisp(library)

        # create pool display
        self.pool = create_dice_list(
            "dicesets/pools/user/starter.yaml")
        self.pool_disp = DiceListDisp(self.pool)

        # create summon display
        dice = self.library_disp.focus.dice
        self.summon_disp = SummonDisp(dice.card)

        # create right column
        right_col = urwid.Pile([
            (17, urwid.LineBox(self.pool_disp, 
                "Pool", "left")),
            (10, urwid.LineBox(self.summon_disp,
                "Summon Information", "left")),
            urwid.SolidFill()]) # PileError workaround

        # create body
        body_cols = urwid.Columns([
            urwid.LineBox(self.library_disp,
                "Dice Library", "left"),
            right_col])
            #right_col], focus_column=1)
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

        # if control arrows, change focused list
        elif key == "right":
            self.contents["body"][0].original_widget.set_focus_column = 1
        elif key == "left":
            self.contents["body"][0].original_widget.set_focus_column = 0
            #self.contents["body"][0].original_widget.set_focus = self.library_disp

    def mouse_event(self, size, event, button, col, row, 
        focus):
        self.contents["body"][0].mouse_event(size, event, 
            button, col, row, focus)
        dice = self.get_focus_widgets()[-2].dice
        self.summon_disp.update(dice.card)

