class Tile():
    """
    Generic tile.
    """
    def is_empty(self):
        return False
    def is_dungeon(self):
        return False
    def is_block(self):
        return False
    def is_occupied(self):
        return False
    def is_reachable(self):
        return False
