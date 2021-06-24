from dice.crests.crest import Crest

class DefenseCrest(Crest):
    """
    A defense crest.
    """
    def __init__(self):
        self.name = "DEFENSE"

    def add_to_pool(self, pool, mult):
        """
        Add the defense defense to pool.
        """
        pool.defense = min(pool.defense+mult, pool.limit)
