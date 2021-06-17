from dicesets_functions import create_player_pool

class Player():
    """
    The player that is playing the duel.
    """
    def __init__(self):
        self.pool = create_player_pool()
