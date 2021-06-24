from dice.crests.crest import Crest

class SummonCrest(Crest):
    """
    A summon crest.
    """
    def __init__(self):
        self.name = "SUMMON"

    def add_to_pool(self, pool, mult):
        """
        Since this is a summon crests, don't add anything
        to the crest pool.
        """
        pass

    def is_summon(self):
        return True
