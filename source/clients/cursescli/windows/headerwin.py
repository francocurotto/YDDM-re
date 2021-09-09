from cursescli.windows.window import Window

class HeaderWin(Window):
    """
    Window for header, turn information.
    """
    def __init__(self, parwin, y ,x):
        super().__init__(parwin, 1, 60, y, x)

    def update(self, engine, stringifier):
        """
        Update window conent.
        """
        self.win.clear()
        header = stringifier.stringify_header(engine.dsm)
        self.win.addstr(0, 0, header)
        self.win.noutrefresh()
