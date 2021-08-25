class SkipGen():
    """
    Generator for skip command.
    """
    def __init__(self):
        self.key = "s"
        self.desc = desc

    def create_command(self, split):
        """
        Create skip command.
        """
        return {"command" : "SKIP"}

desc = "\
- SKIP COMMAND: s\n\
    - s: skip dimension or reply"
