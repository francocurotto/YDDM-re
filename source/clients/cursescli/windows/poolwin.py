from cursescli.windows.boxedwin import BoxedWin

class PoolWin(BoxedWin):
    """
    Window to display pool.
    """
    def __init__(self, parwin, y, x):
        super().__init__(parwin, 17, 66, y, x, "Dice Pool")

    def update(self, engine, stringifier):
        """
        Update window content.
        """
        super().update()
        # create string
        player = engine.dsm.state.player
        string = stringifier.stringify_dicepool(player)
        # update window
        self.addstr(string)
