from dice.crests.crest import Crest

class TrapCrest(Crest):
    """
    A trap crest.
    """
    def __init__(self):
        self.name = "TRAP"

    def add_to_pool(self, pool, mult):
        """
        Add the trap crest to pool.
        """
        pool.trap = min(pool.trap+mult, pool.limit)
