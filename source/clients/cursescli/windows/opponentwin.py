from cursescli.windows.boxedwin import BoxedWin

class OpponentWin(BoxedWin):
    """
    Window to display opponent information.
    """
    def __init__(self, parwin, y, x):
        super().__init__(parwin, 4, 32, y, x, "Opponent")

    def update(self, engine, stringifier):
        """
        Update window content.
        """
        super().update()
        # create string with crest pool info
        crestpool = engine.dsm.state.opponent.crestpool
        string = stringifier.stringify_crestpool(crestpool)
        # add monster lord info
        duel = engine.duel
        ml   = engine.dsm.state.opponent.ml 
        string += "\n"
        string += stringifier.stringify_monster_lord(duel,ml)
        # update window
        self.addstr(string)
