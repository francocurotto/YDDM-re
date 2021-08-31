class QuitGen():
    """
    Generator for quit command.
    """
    def __init__(self):
        self.key = "q"
        self.desc = desc

    def create_command(self, split):
        """
        Quit the game.
        """
        print("Bye!")
        exit()

desc = "\
- QUIT COMMAND: q\n\
    - q: quit game"
