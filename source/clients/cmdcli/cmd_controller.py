import readline # for input history
from cmdcli.text_controller import TextController

class CmdController(TextController):
    """
    Input controller for command line interface.
    """
    def get_text_input(self):
        """
        Get input from user text
        """
        self.view.print_header()
        return input(">> ")

