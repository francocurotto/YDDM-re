import urwid

class DiscardWidget(urwid.LineBox):
    """
    Window shown with the discard dialog.
    """
    def __init__(self, builder):
        # instruciont text
        text = urwid.Text(
            "Pool not filled. Discard changes?", "center")
        # discard button
        discardbut = urwid.Button("Yes", exit_builder)
        # cancel button
        cancelbut = urwid.Button("No", return_builder, 
            builder)
        # buttons line
        buttons = urwid.Columns([urwid.Divider(),
            (7,discardbut), urwid.Divider(), (6,cancelbut), 
            urwid.Divider()])
        # widgets pile
        self.pile = urwid.Pile([urwid.Divider(), text,
            urwid.Divider(), buttons, urwid.Divider()])
        super().__init__(self.pile)

def exit_builder(button):
    raise urwid.ExitMainLoop()

def return_builder(button, builder):
    builder.return_builder()
