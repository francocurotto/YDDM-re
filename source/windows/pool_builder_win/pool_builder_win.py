import urwid
from globvars import library
from dicesets_functions import create_dice_list
from dice_lib_disp import DiceLibDisp
from pool_disp import PoolDisp
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
        self.pool_disp = PoolDisp(self.pool)

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
        body = urwid.Padding(body_cols, align="center",
            width=67*2)
    
        # create footer
        footer = urwid.Text("↑,↓:Select dice | " +
            "←,→: Remove,add dice | " +
            "CTRL+←,→:Change list")
        super().__init__(body, footer=footer)

    def keypress(self, size, key):
        # if up/down arrows, change summon display
        if key in ["up", "down"]:
            self.contents["body"][0].keypress(size, key)

        # if control arrows, change focused list
        elif key == "ctrl right" and \
            not self.pool_disp.empty():
            self.contents["body"][0].keypress(size, "right")
        elif key == "ctrl left":
            self.contents["body"][0].keypress(size, "left")

        # if right and lib focused, add dice to pool
        elif key == "right" and self.lib_focused():
            dice = self.get_focus_widgets()[-2].dice
            success = self.pool_disp.add_dice(dice)
            if not success:
                #TODO: add pool full message
                pass

        # if left and pool focused, remove dice
        elif key == "left" and self.pool_focused():
            self.pool_disp.remove_dice()
            # if pool is empty, return to library
            if self.pool_disp.empty():
                self.contents["body"][0].keypress(size, "left")
           
        # update summon display after any key
        self.update_summon_disp()

    def lib_focused(self):
        """
        True if library is currently focused.
        """
        focused = self.get_focus_widgets()[-3].original_widget
        return self.library_disp is focused

    def pool_focused(self):
        """
        True if pool is currently focused.
        """
        focused = self.get_focus_widgets()[-3].original_widget
        return self.pool_disp is focused

    def mouse_event(self, size, event, button, col, row, 
        focus):
        self.contents["body"][0].mouse_event(size, event, 
            button, col, row, focus)
        dice = self.get_focus_widgets()[-2].dice
        self.update_summon_disp()

    def update_summon_disp(self):
        dice = self.get_focus_widgets()[-2].dice
        self.summon_disp.update(dice.card)
        
