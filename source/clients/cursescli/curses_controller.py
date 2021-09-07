from cmdcli.text_controller import TextController

class CursesController(TextController):
    """
    Input controller for curses interface.
    """
    def __init__(self, view, engine, stringifier):
        super().__init__(view, engine, stringifier)

    def get_text_input(self):
        """
        Get input from user text.
        """
        return self.view.inputwin.get_input()
