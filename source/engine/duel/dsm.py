for duel.roll_state import RollState

class DuelStateMachine():
    """
    Controls in which state is the duel.
    """
    def __init__(self, duel):
        # duel, players
        self.duel = duel
        self.player = self.duel.player1
        self.opponent = self.duel.player2
        self.turn = 1
        
        # current state
        self.state = RollState(self.duel, 
            self.player, self.opponent)

    def update(self, cmd):
        """
        Update state machine given command cmd.
        """
        reply = self.state.update(command)
        if reply["newturn"]:
            self.adv_turn()

    def adv_turn(self):
        """
        Advance to next turn. Increment turn counter and  
        swap player and opponent.
        """
        self.turn += 1
        temp_player = self.player
        self.player = self.opponent
        self.opponent = temp_player
