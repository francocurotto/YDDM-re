from duel.roll_state import RollState

class DuelStateMachine():
    """
    Controls in which state is the duel.
    """
    def __init__(self, duel):
        # duel, players
        self.duel = duel
        self.turn = 1
        
        # current state
        self.state = RollState(self.duel, self.duel.player1,
            self.duel.player2)

    def update(self, cmd):
        """
        Update state machine given command cmd.
        """
        reply, newstate = self.state.update(cmd)
        self.turn += reply["newturn"] # incr turn counter
        self.state = newstate
        return reply
