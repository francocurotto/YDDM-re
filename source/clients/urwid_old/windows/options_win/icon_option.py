import urwid
from globvars import icons
from icon_functions import load_icons

class IconOption(urwid.Pile):
    """
    Section for the selection of icons in the game.
    """
    def __init__(self, settings):
        # create icon test
        test = urwid.Text("")

        # create option text
        text = urwid.Text("Icons: ")

        # create radio buttons
        options = ["emoji", "unicode", "ascii"]
        self.group = []
        for option in options:
            state = option == settings["display_type"]
            rb = urwid.RadioButton(self.group, option, state)
            urwid.connect_signal(rb, "postchange",  
                update_icons, user_args=[settings, test])

        # create columns
        col_list = [("pack", text)]
        for rb in self.group:
            width = len(rb.get_label())
            col_list.append((width+8, rb))
        cols = urwid.Columns(col_list)

        # option desciption
        desc = urwid.Text("Icon test (should show no " +
        "spaces between icons and no ⍰ icon. If not, use " +
        "other setting):")

        # run test for the first time
        for rb in self.group:
            update_icons(settings, test, rb, rb.state)

        # focus the selected widget
        for rb in self.group:
            if rb.state:
                cols.set_focus(rb)

        super().__init__([cols, urwid.Divider(), desc, test])

def update_icons(settings, test, rb, state):
    """
    Update the icons in the settings and in the icon test
    when the player changes the option.
    """
    # only do this if radio button is activated
    if not rb.state:
        return

    # get the selected display type
    sel_display = rb.get_label()

    # update the settings in the window variable
    settings["display_type"] = sel_display

    # get selected icons
    sel_icons = icons[sel_display]

    # generate string
    str_list = []
    for icon in sel_icons.values():
        str_list.append(icon)
    string = "".join(str_list)

    # set the string to the test text
    test.set_text(string)
