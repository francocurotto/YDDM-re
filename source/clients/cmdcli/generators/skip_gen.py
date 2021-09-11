from cmdcli.generators.generator import Generator

class SkipGen(Generator):
    """
    Generator for skip command.
    """
    def __init__(self):
        self.key = "s"
        super().__init__()

    def create_command(self, split):
        """
        Create skip command.
        """
        return {"command" : "SKIP"}
