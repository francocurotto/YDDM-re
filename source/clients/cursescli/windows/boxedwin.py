from cursescli.windows.window import Window, create_derwin

class BoxedWin(Window):
    """
    A window surrounded by a box.
    """
    def __init__(self, parwin, dy, dx, y, x, title):
        # create box
        self.box = create_derwin(parwin, dy, dx, y, x)
        self.box.border()
        self.box.addstr(0, 2, " " + title + " ")

        # create actual window
        super().__init__(parwin, dy-2, dx-2, y+1, x+1)

    def update(self):
        """
        Update window content.
        """
        super().update()
        self.box.noutrefresh()

