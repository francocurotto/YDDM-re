from cursescli.windows.boxedwin import BoxedWin

class DungeonWin(BoxedWin):
    """
    Window to display the dungeon.
    """
    def __init__(self, parwin, y, x):
        super().__init__(parwin, 25, 36, y, x, "Dungeon")

    def update(self, engine, stringifier):
        """
        Update window content.
        """
        super().update()
        # create string
        string = stringifier.stringify_dungeon(engine.duel)
        # update window
        self.addstr(string)
