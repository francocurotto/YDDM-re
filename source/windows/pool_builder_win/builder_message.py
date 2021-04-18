import urwid

class BuilderMessage(urwid.Text):
    """
    Message block for pool builder window. Handles finish 
    with discard.
    """
    _selectable = True
    def keypress(self, size, key):
        if key == "y":
            from globvars import main_win
            main_win.switch_title()
            return
        return key

