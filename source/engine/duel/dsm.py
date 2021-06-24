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
        self.check_new_turn(newstate)
        self.state = newstate
        return reply

    def check_new_turn(self, newstate):
        """
        Check if new turn has passed. Increment turn counter
        if it has.
        """
        if self.state.player != newstate.player:
            self.turn += 1
