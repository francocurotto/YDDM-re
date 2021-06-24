class CrestPool():
    """
    The crest pool of a player.
    """
    limit = 99
    def __init__(self):
        self.movement = 0
        self.attack   = 0
        self.defense  = 0
        self.magic    = 0
        self.trap     = 0

    def add_crests(self, side):
        """
        Adds the crests from the a dice side to the crest 
        pool.
        """
        side.crest.add_to_pool(self, side.mult)
