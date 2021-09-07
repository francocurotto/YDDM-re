class WaitGen():
    """
    Generator for wait command.
    """
    def __init__(self):
        self.key = "w"
        self.desc = desc

    def create_command(self, split):
        """
        Create wait command.
        """
        return {"command" : "WAIT"}

desc = "\
- WAIT COMMAND: w\n\
    - w: do not reply to an attack"
