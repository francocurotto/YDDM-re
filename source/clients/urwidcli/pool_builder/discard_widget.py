import urwid

class DiscardWidget(urwid.LineBox):
    """
    Window shown with the discard dialog.
    """
    def __init__(self):
        self.text = urwid.Text(
            "Pool not filled. Discard changes?", "center")
        self.pile = urwid.Pile([urwid.Divider(), self.text,
            urwid.Divider(), urwid.Divider(), urwid.Divider()])
        super().__init__(self.pile)

