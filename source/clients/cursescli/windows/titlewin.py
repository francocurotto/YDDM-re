from cursescli.windows.window import Window

class TitleWin(Window):
    """
    Window for user input.
    """
    def __init__(self, parwin, y ,x):
        super().__init__(parwin, 1, 8, y, x)

    def update(self, engine, stringifier):
        """
        Update window conent.
        """
        super().update()
        self.addstr("YDDM-re")
