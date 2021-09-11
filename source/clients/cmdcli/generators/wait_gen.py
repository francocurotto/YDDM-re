from cmdcli.generators.generator import Generator

class WaitGen(Generator):
    """
    Generator for wait command.
    """
    def __init__(self):
        self.key = "w"
        super().__init__()

    def create_command(self, split):
        """
        Create wait command.
        """
        return {"command" : "WAIT"}
