class Crest():
    """
    A generic crest from a dice.
    """
    def __init__(self, type):
        self.type = type

    def is_summon(self):
        """
        By default, generic crest is not a summon crest.
        """
        return False
