from dungeon.tiles.tile import Tile

class EmptyTile(Tile):
    """
    tile with no dungeon path in it.
    """
    def is_empty(self):
        return True
        
