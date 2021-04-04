class SummonCard():
    """
    Object that contains the information of a summon.
    """
    def __init__(self, info):
        self.name = info["NAME"]
        self.type = info["TYPE"]
        self.level = info["LEVEL"]
        # TODO: change to proper ability class
        self.ability = info["ABILITY"]
