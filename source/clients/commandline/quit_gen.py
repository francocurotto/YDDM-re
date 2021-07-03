from stringifier import Stringifier

class QuitGen():
    """
    Generator for quit command.
    """
    def __init__(self):
        self.key = "q"
        self.desc = desc

    def create_command(self, engine, split):
        """
        Quit the game.
        """
        print("Bye!")
        exit()

desc = "\
- QUIT COMMAND: q\n\
    - quit game"
