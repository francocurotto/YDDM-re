import urwid
from globvars import icons
from icon_functions import load_icons

class IconOption(urwid.Pile):
    """
    Section for the selection of icons in the game.
    """
    def __init__(self):
        # icon test
        self.test = urwid.Text("")

        # create radio buttons
        options = ["emoji", "unicode", "ascii"]
        self.group = []
        for option in options:
            rb = urwid.RadioButton(self.group, option)
            urwid.connect_signal(rb, "postchange", set_test,
                self.test)

        # add option text
        text = urwid.Text("Icons: ")

        # create columns
        col_list = [("pack", text)]
        for rb in self.group:
            width = len(rb.get_label())
            col_list.append((width+8, rb))
        cols = urwid.Columns(col_list)

        # option pad
        pad = urwid.Padding(cols)

        # option desciption
        desc = urwid.Text("Icon test (should show no " +
        "spaces between icons and no ⍰ icon. If not, use " +
        "other setting):")

        #self.set_test()

        super().__init__([pad, desc, self.test])

def set_test(rb, state, test):
    """
    Change the text on the icon test accoring to the
    radio button activated.
    """
    # only do this if radio button is activated
    if not rb.state:
        return

    # get the selected display type
    sel_display = rb.get_label()

    # get selected icons
    sel_icons = icons[sel_display]

    # generate string
    str_list = []
    for icon in sel_icons.values():
        str_list.append(icon)
    string = "".join(str_list)

    # set tne string to the test text
    test.set_text(string)
