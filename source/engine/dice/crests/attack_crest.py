from dice.crests.crest import Crest

class AttackCrest(Crest):
    """
    An attack crest.
    """
    def __init__(self):
        self.name = "ATTACK"

    def add_to_pool(self, pool, mult):
        """
        Add the attack crest to pool.
        """
        pool.attack = min(pool.attack+mult, pool.limit)
