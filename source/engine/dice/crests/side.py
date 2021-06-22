from dice.dicevars import crest_dict
from dice.crests.crest import Crest
from dice.crests.summon_crest import SummonCrest

class Side():
    """
    A side from a dice. Includes the crest and the 
    multiplier.
    """
    def __init__(self, side_string):
        crest_char = side_string[0]
        # create crest
        if crest_char == "S":
            self.crest = SummonCrest()
        else:
            self.crest = Crest(crest_dict[crest_char])
        # create multiplier
        if len(side_string) > 1:
            self.multiplier = int(side_string[1:])
        else:
            self.multiplier = 1
