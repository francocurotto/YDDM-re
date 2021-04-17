import urwid
import copy
from globvars import library
from dice import Dice
from dicesets_functions import create_player_pool
from dice_list_disp import DiceListDisp
from pool_disp import PoolDisp
from summon_disp import SummonDisp

class PoolBuilderWin(urwid.Frame):
    """
    Window where the player can build dice pools.
    """
    def __init__(self):
        # create library display
        self.lib_disp = DiceListDisp(library.values(), 
            disp_id=True)

        # create pool display
        self.pool = create_player_pool()
        self.pool_disp = PoolDisp(self.pool)

        # create summon display
        dice = self.lib_disp.focus.dice
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
            urwid.LineBox(self.lib_disp, "Dice Library",
                "left"),
            right_col])
        body = urwid.Padding(body_cols, align="center",
            width=67*2)
    
        # create footer
        self.message = urwid.Text("")
        controls = urwid.Text("↑,↓:Select dice | " +
            "←,→:Change list | " +
            "SPACE: Remove,add dice")
        footer = urwid.Pile([self.message, controls])
        super().__init__(body, footer=footer)

    def keypress(self, size, key):
        key = super().keypress(size, key)

        # reset message
        self.message.set_text("")

        # if space and lib focused, add dice to pool
        if key == " " and self.lib_focused():
            #dice = self.get_focus_widgets()[-2].dice
            dice = self.lib_disp.get_focus_widgets()[0].dice
            dice = copy.deepcopy(dice)
            success = self.pool_disp.add_dice(dice)
            if not success:
                self.message.set_text("Pool is full.")

        # if space and pool focused, remove dice
        elif key == " " and self.pool_focused():
            self.pool_disp.remove_dice()

        # if players what to finish
        elif key == "f":
            if self.pool_disp.pool.full():
                self.pool_disp.pool.save()
                from globvars import main_win
                main_win.switch_title()

        # update summon display after any key
        self.update_summon_disp()

    def lib_focused(self):
        """
        True if library is currently focused.
        """
        focus = self.get_focus_widgets()[-3].original_widget
        return self.lib_disp is focus

    def pool_focused(self):
        """
        True if pool is currently focused.
        """
        focus = self.get_focus_widgets()[-3].original_widget
        return self.pool_disp is focus

    def mouse_event(self, size, event, button, col, row, 
        focus):
        self.contents["body"][0].mouse_event(size, event, 
            button, col, row, focus)
        dice = self.get_focus_widgets()[-2].dice
        self.update_summon_disp()

    def update_summon_disp(self):
        try:
            dice = self.get_focus_widgets()[-2].dice
        # check in case focused widget has no dice
        except AttributeError:
            return
        self.summon_disp.update(dice.card)
        
