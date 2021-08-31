from commandline.text_controller import TextController

class CliController(TextController):
    """
    Input controller for command line interface.
    """
    def get_text_input(self):
        """
        Get input from user text
        """
        return input(">> ")
