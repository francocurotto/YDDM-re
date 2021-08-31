class GuardGen():
    """
    Generator for guard command.
    """
    def __init__(self):
        self.key = "g"
        self.desc = desc

    def create_command(self, split):
        """
        Create guard command.
        """
        return {"command" : "GUARD"}

desc = "\
- GUARD COMMAND: g\n\
    - g: defend against attack"
