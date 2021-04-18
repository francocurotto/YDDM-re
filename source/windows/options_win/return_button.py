import urwid
from menu import ListEntry

class ReturnButton(urwid.Padding):
    """
    Button to return to main window.
    """
    def __init__(self):
        button = ListEntry("Return", ret_main_win)
        width = len(button.get_text()[0])
        button = urwid.AttrMap(button, None,
            focus_map="focused")
        super().__init__(button, "center", width)

def ret_main_win(button):
    from globvars import main_win
    main_win.switch_title()
