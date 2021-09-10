from curses.textpad import Textbox
from cursescli.windows.window import Window, create_derwin

class InputWin(Window):
    """
    Window for user input.
    """
    def __init__(self, parwin, y ,x):
        super().__init__(parwin, 1, 21, y, x)
        # add textbox
        self.boxwin = create_derwin(self.win, 1, 18, 0, 3)
        self.textbox = Textbox(self.boxwin)

    def update(self, engine, stringifier):
        """
        Update window conent.
        """
        super().update()
        self.addstr(">> ")

    def get_input(self):
        """
        Get text input from textbox.
        """
        self.textbox.edit()
        string = self.textbox.gather()
        self.boxwin.clear()
        self.boxwin.move(0,0)
        return string
