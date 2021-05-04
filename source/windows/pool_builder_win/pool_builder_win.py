import urwid
import copy
from globvars import library
from builder_message import BuilderMessage
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

        # create boxed widgets
        lib_disp = urwid.LineBox(self.lib_disp, 
            "Dice Library", "left")
        pool_disp = urwid.LineBox(self.pool_disp, 
            "Pool", "left")
        summon_disp = urwid.LineBox(self.summon_disp,
            "Summon Information", "left")

        # create right column
        right_col = urwid.Pile([(17,pool_disp), summon_disp])

        # create body
        body_cols = urwid.Columns([lib_disp, right_col])
        body = urwid.Padding(body_cols, align="center",
            width=67*2)
    
        # create footer
        self.message = BuilderMessage("")
        controls = urwid.Text(
            "↑,↓:Select dice | " +
            "←,→:Change list | " +
            "SPACE: Remove,add dice | " + 
            "f: finish")
        footer = urwid.Pile([self.message, controls])

        super().__init__(body, footer=footer)

    def keypress(self, size, key):
        key = super().keypress(size, key)

        # reset message widget
        self.reset_message()

        # if space and lib focused, add dice to pool
        if key == " " and self.lib_focused():
            self.add_dice_to_pool()

        # if space and pool focused, remove dice
        elif key == " " and self.pool_focused():
            self.pool_disp.remove_dice()

        # if players what to finish
        elif key == "f":
            self.try_to_finish()

        # update summon display after any key
        self.update_summon_disp()

    def reset_message(self):
        """
        Reset message text. Also, if focus was in the footer,
        user stopped finish with discard, hence, return focus
        to body.
        """
        # reset message text
        self.message.set_text("")

        # return focus to body
        if self.focus_position == "footer":
            self.focus_position = "body"

    def lib_focused(self):
        """
        True if library is currently focused.
        """
        focus = self.get_focus_widgets()[-3].original_widget
        return focus is self.lib_disp

    def pool_focused(self):
        """
        True if pool is currently focused.
        """
        focus = self.get_focus_widgets()[-3].original_widget
        return focus is self.pool_disp

    def add_dice_to_pool(self):
        """
        Add a copy of the focused dice on library to the 
        pool. If pool is full, report in message widget.
        """
        # get a copy of the focused dice in library
        dice = self.lib_disp.get_focus_widgets()[0].dice
        dice = copy.deepcopy(dice)

        # try to add the dice. If pool full, report.
        success = self.pool_disp.add_dice(dice)
        if not success:
            self.message.set_text("Pool is full.")

    def try_to_finish(self):
        """
        Attempt to finish with the pool building. If pool is
        full, save dice pool and return to main window. If
        pool not full, setup message for discard 
        confirmation.
        """
        # if pool full, finish
        if self.pool_disp.pool.full():
            self.pool_disp.pool.save()
            from globvars import main_win
            main_win.switch_title()
        # if pool not full, confirm discard
        else:
            self.message.set_text("Pool not full. Discard " + 
                "changes? [y:yes]")
            self.focus_position = "footer"

    def update_summon_disp(self):
        """
        Update the summon display with the current dice in 
        focus. If focus is not dice, do nothing.
        """
        try:
            dice = self.get_focus_widgets()[-2].dice
        # check in case focused widget has no dice
        except AttributeError:
            return
        self.summon_disp.update(dice.card)
        
    def mouse_event(self, size, event, button, col, row, 
        focus):
        self.contents["body"][0].mouse_event(size, event, 
            button, col, row, focus)
        dice = self.get_focus_widgets()[-2].dice
        self.update_summon_disp()
