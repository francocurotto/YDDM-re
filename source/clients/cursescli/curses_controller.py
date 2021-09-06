from commandline.text_controller import TextController

class CursesController(TextController):
    """
    Input controller for curses interface.
    """
    def __init__(self, view, engine, stringifier):
        super().__init__(view, engine, stringifier)
        self.inputwin = self.view.inputwin
        self.inputbox = self.inputwin.inputbox

    def get_text_input(self):
        """
        Get input from user text.
        """
        self.inputwin.win.move(0,0)
        self.inputbox.edit()
        string = self.inputbox.gather()
        self.inputwin.win.clear()
        self.inputwin.win.refresh()
        return string
