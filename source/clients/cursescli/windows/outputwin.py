from cursescli.windows.boxedwin import BoxedWin

class OutputWin(BoxedWin):
    """
    Window to display text output.
    """
    def __init__(self, parwin, y, x):
        super().__init__(parwin, 14, 65, y, x, "Output")
        self.textbuffer = []

    def update(self, engine, stringifier):
        """
        Update window content.
        """
        super().update()
        string = "\n".join(self.textbuffer[-12:])
        self.addstr(string)
    
    def print_string(self, string):
        """
        Add string to window buffer.
        """
        newlines = string.split("\n")
        self.textbuffer += newlines
