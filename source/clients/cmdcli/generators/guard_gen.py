from cmdcli.generators.generator import Generator

class GuardGen(Generator):
    """
    Generator for guard command.
    """
    def __init__(self):
        self.key = "g"
        super().__init__()

    def create_command(self, split):
        """
        Create guard command.
        """
        return {"command" : "GUARD"}
