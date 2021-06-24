from dice.crests.crest import Crest

class MagicCrest(Crest):
    """
    A magic crest.
    """
    def __init__(self):
        self.name = "MAGIC"

    def add_to_pool(self, pool, mult):
        """
        Add the magic crest to pool.
        """
        pool.magic = min(pool.magic+mult, pool.limit)
