import urwid
import yaml
from globvars import saved_settings_path
from menu import ListEntry

class ReturnButton(urwid.Padding):
    """
    Button to return to main window.
    """
    def __init__(self, settings):
        button = ListEntry("Return", ret_main_win, settings)
        width = len(button.get_text()[0])
        button = urwid.AttrMap(button, None,
            focus_map="focused")
        super().__init__(button, "center", width)

def ret_main_win(button, settings):
    # first save updated settings
    with open(saved_settings_path, "w") as f:
        yaml.dump(settings, f)

    from globvars import main_win
    main_win.switch_title()
