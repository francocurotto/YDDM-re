from cursescli.windows.boxedwin import BoxedWin

class PlayerWin(BoxedWin):
    """
    Window to display pool.
    """
    def __init__(self, parwin, y, x):
        super().__init__(parwin, 4, 32, y, x, "Player")

    def update(self, engine, stringifier):
        """
        Update window content.
        """
        super().update()
        # create string with crest pool info
        crestpool = engine.dsm.state.player.crestpool
        string = stringifier.stringify_crestpool(crestpool)
        # add monster lord info
        duel = engine.duel
        ml   = engine.dsm.state.player.ml 
        string += "\n"
        string += stringifier.stringify_monster_lord(duel,ml)
        # update window
        self.addstr(string)
        self.win.noutrefresh()
