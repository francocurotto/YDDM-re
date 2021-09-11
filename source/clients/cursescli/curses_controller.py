from cmdcli.text_controller import TextController
from cursescli.curses_printgen import CursesPrintGen

class CursesController(TextController):
    """
    Input controller for curses interface.
    """
    def __init__(self, view, engine, stringifier):
        super().__init__(view, engine, stringifier)
        # replace printgenerator with striped one
        self.printgen = CursesPrintGen(engine, stringifier)

    def get_text_input(self):
        """
        Get input from user text.
        """
        return self.view.inputwin.get_input()
