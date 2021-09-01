import readline # for input history
from commandline.text_controller import TextController

class CliController(TextController):
    """
    Input controller for command line interface.
    """
    def get_text_input(self):
        """
        Get input from user text
        """
        self.view.print_string(self.get_header(), end="\n")
        return input(">> ")

    def get_header(self):
        """
        Create string of information after every command.
        """
        string  = "<"
        string += str(self.engine.dsm.state.player.name)
        string += "[p"
        string += str(self.engine.dsm.state.player.id)
        string += "] | state:"
        string += self.engine.dsm.state.name
        string += " | turn:"
        string += str(self.engine.dsm.turn)
        string += "> (l:list command)"
        return string


