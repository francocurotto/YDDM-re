from dice.crests.crest import Crest

class MovementCrest(Crest):
    """
    A movement crest.
    """
    def __init__(self):
        self.name = "MOVEMENT"

    def add_to_pool(self, pool, mult):
        """
        Add the movement crest to pool.
        """
        pool.movement = min(pool.movement+mult, pool.limit)

