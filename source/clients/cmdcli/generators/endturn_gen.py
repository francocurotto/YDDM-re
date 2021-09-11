from cmdcli.generators.generator import Generator

class EndturnGen():
    """
    Generator for endturn command.
    """
    def __init__(self):
        self.key = "e"
        super().__init__()

    def create_command(self, split):
        """
        Quit the game.
        """
        return {"command" : "ENDTURN"}
