from dice.crests.crest import Crest

class SummonCrest(Crest):
    """
    A summon crest.
    """
    def __init__(self):
        super().__init__("SUMMON")

    def is_summon(self):
        return True
