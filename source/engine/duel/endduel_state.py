from duel.duel_state import DuelState

class EndDuelState(DuelState):
    """
    State were the duel has ended and no more actions are
    allowed.
    """
    def __init__(self, duel, player, opponent):
        super().__init__(duel, player, opponent)
        self.name = "ENDDUEL"
        self.cmddict = {}

