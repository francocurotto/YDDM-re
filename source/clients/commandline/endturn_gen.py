class EndturnGen():
    """
    Generator for endturn command.
    """
    def __init__(self):
        self.key = "e"
        self.desc = desc

    def create_command(self, split):
        """
        Quit the game.
        """
        return {"command" : "ENDTURN"}

desc = "\
- ENDTURN COMMAND: e\n\
    - e: end turn"
